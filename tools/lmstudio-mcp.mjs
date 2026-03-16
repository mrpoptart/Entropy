#!/usr/bin/env node

import { McpServer } from "@modelcontextprotocol/sdk/server/mcp.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";
import { z } from "zod";

const LM_STUDIO_URL = process.env.LM_STUDIO_URL || "http://127.0.0.1:1234";

async function chatWithLocal(prompt, systemPrompt) {
  const messages = [];
  if (systemPrompt) {
    messages.push({ role: "system", content: systemPrompt });
  }
  messages.push({ role: "user", content: prompt });

  const res = await fetch(`${LM_STUDIO_URL}/v1/chat/completions`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({
      messages,
      temperature: 0.3,
      max_tokens: 4096,
    }),
  });

  if (!res.ok) {
    const text = await res.text();
    throw new Error(`LM Studio error ${res.status}: ${text}`);
  }

  const data = await res.json();
  return data.choices[0].message.content;
}

const server = new McpServer({
  name: "lmstudio-local",
  version: "1.0.0",
});

server.tool(
  "continuity_check",
  "Check a chapter draft against the outline for contradictions, timeline errors, and inconsistencies. Offloads this work to the local LLM to save tokens.",
  {
    chapter_text: z.string().describe("The chapter draft text to check"),
    outline_entry: z.string().describe("The outline entry for this chapter"),
    additional_context: z.string().optional().describe("Any additional context (e.g., previous chapter summary, character details)"),
  },
  async ({ chapter_text, outline_entry, additional_context }) => {
    const system = `You are a continuity checker for a fantasy novel. Your job is to compare a chapter draft against its outline entry and flag:
- Contradictions between draft and outline (names, events, locations, timeline)
- Characters present in the draft but not mentioned in the outline (or vice versa)
- Location names that don't match established names
- Timeline inconsistencies
- Reservoir percentage mismatches

Be specific. Quote the conflicting passages. Only flag real issues, not stylistic differences.`;

    let prompt = `## Outline Entry\n${outline_entry}\n\n## Chapter Draft\n${chapter_text}`;
    if (additional_context) {
      prompt = `## Additional Context\n${additional_context}\n\n${prompt}`;
    }

    const result = await chatWithLocal(prompt, system);
    return { content: [{ type: "text", text: result }] };
  }
);

server.tool(
  "summarize_reviews",
  "Summarize reviewer agent output into a concise revision brief. Offloads summarization to the local LLM.",
  {
    review_text: z.string().describe("The combined review output from agents"),
  },
  async ({ review_text }) => {
    const system = `You are an editorial assistant. Summarize the following review feedback into a concise revision brief. Group issues by priority (Critical / High / Medium / Low). For each issue, state what's wrong and where, in one sentence. Remove redundancy across reviewers.`;

    const result = await chatWithLocal(review_text, system);
    return { content: [{ type: "text", text: result }] };
  }
);

server.tool(
  "local_llm_query",
  "Send a freeform prompt to the local LLM. Use for brainstorming, checking facts against provided text, or any task that doesn't need Opus-level reasoning.",
  {
    prompt: z.string().describe("The prompt to send"),
    system_prompt: z.string().optional().describe("Optional system prompt"),
  },
  async ({ prompt, system_prompt }) => {
    const result = await chatWithLocal(prompt, system_prompt);
    return { content: [{ type: "text", text: result }] };
  }
);

const transport = new StdioServerTransport();
await server.connect(transport);
