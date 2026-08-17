# Palimnote Skills

Palimnote Skills is a catalog of portable agent skills — self-contained instruction packages following the SKILL.md convention. Each skill is usable in Claude Code (drop the folder into `.claude/skills/<name>/`) or any agent runtime supporting the convention, and each one lives in its own repository.

## Writing

| Skill | Description |
| --- | --- |
| [ai-writing-humanizer](https://github.com/hyderhusainarastu/ai-writing-humanizer) | Detect AI-sounding patterns in prose and rewrite in an authentic human voice, with channel-specific rules |
| [author-style-profile-mining](https://github.com/hyderhusainarastu/author-style-profile-mining) | Mine a writing corpus for an author's stylistic tics and turn them into imitation or avoidance rules |
| [structural-checklist-from-exemplars](https://github.com/hyderhusainarastu/structural-checklist-from-exemplars) | Derive a reusable structural checklist for any document genre by comparing exemplar documents |
| [manuscript-mechanical-qa-sweep-pipeline](https://github.com/hyderhusainarastu/manuscript-mechanical-qa-sweep-pipeline) | Mechanical pre-review QA sweeps for long-form manuscripts: leak greps, claim-verb discipline, compile gate |

## Research

| Skill | Description |
| --- | --- |
| [quote-verification-toolkit](https://github.com/hyderhusainarastu/quote-verification-toolkit) | Verify quoted excerpts against source texts, tolerant of PDF line-wraps, Unicode punctuation, and elision |
| [source-intake-pipeline](https://github.com/hyderhusainarastu/source-intake-pipeline) | Gated intake pipeline for research sources: metadata verification, citability classification, dedupe, provenance |
| [citation-lead-mining-and-dedup](https://github.com/hyderhusainarastu/citation-lead-mining-and-dedup) | Mine candidate references and idea leads from source text into deduplicated follow-up tables |
| [source-authority-hierarchy](https://github.com/hyderhusainarastu/source-authority-hierarchy) | A tiered authority hierarchy for resolving conflicts between sources when evidence disagrees |
| [empirical-study-design-and-gold-set-toolkit](https://github.com/hyderhusainarastu/empirical-study-design-and-gold-set-toolkit) | Design empirical evaluations end to end and build gold-standard sets with blinding and leakage controls |
| [scholarly-metadata-resolution-pattern](https://github.com/hyderhusainarastu/scholarly-metadata-resolution-pattern) | Resolve bibliographic metadata across Crossref, OpenAlex, Google Books, and Open Library with fallback ordering |

## Orchestration

| Skill | Description |
| --- | --- |
| [gated-multi-agent-review-lifecycle](https://github.com/hyderhusainarastu/gated-multi-agent-review-lifecycle) | A gate lifecycle for multi-agent work: structured verdicts, failure routing, escalation, no self-approval |
| [agent-brief-schema-for-specialist-roles](https://github.com/hyderhusainarastu/agent-brief-schema-for-specialist-roles) | A fixed briefing schema for specialist agents: scope, inputs, tools, output contract, acceptance tests |
| [adversarial-peer-review-role](https://github.com/hyderhusainarastu/adversarial-peer-review-role) | An adversarial reviewer role: severity taxonomy, evidence citations, disconfirmation duty |

## Governance

| Skill | Description |
| --- | --- |
| [legacy-plan-reconciliation-matrix](https://github.com/hyderhusainarastu/legacy-plan-reconciliation-matrix) | Audit an outdated plan against current evidence with a REUSE, REVISE, REJECT, DEFER, VERIFY matrix |
| [governance-records-ledger-conventions](https://github.com/hyderhusainarastu/governance-records-ledger-conventions) | Append-only conventions for decision logs, task ledgers, and open-question files in long-running projects |
| [evidence-ledger-and-phase-handoff-convention](https://github.com/hyderhusainarastu/evidence-ledger-and-phase-handoff-convention) | Evidence ledgers and phase-handoff documents that pass auditable context between sessions or agents |
| [pre-publication-review-gate-checklist](https://github.com/hyderhusainarastu/pre-publication-review-gate-checklist) | Pre-launch review gate: claim accuracy, accessibility, privacy, and synthetic demo-data disclosure |
| [ai-project-cost-modeling](https://github.com/hyderhusainarastu/ai-project-cost-modeling) | A structured cost model for AI-assisted projects: category taxonomy across low, base, and high scenarios |

## Engineering

| Skill | Description |
| --- | --- |
| [llm-routing-and-judge-eval-harness-pattern](https://github.com/hyderhusainarastu/llm-routing-and-judge-eval-harness-pattern) | Provider-agnostic LLM routing with deterministic fallback, plus an LLM-as-judge eval harness with gold sets |
| [accessible-dialog-focus-trap-primitives](https://github.com/hyderhusainarastu/accessible-dialog-focus-trap-primitives) | Accessible React dialog primitives: focus trap, escape handling, focus restoration, live-region announcements |
| [nextjs-cloudflare-workers-landing-site-setup](https://github.com/hyderhusainarastu/nextjs-cloudflare-workers-landing-site-setup) | Wire a Next.js landing site onto Cloudflare Workers with wrangler and Drizzle, from scratch |
| [context-window-text-chunking](https://github.com/hyderhusainarastu/context-window-text-chunking) | Paragraph-boundary-aware text chunking for fitting long documents into LLM context windows |

## How to use

Clone the individual skill's repository, then copy its folder into your runtime's skills directory (for Claude Code, `.claude/skills/<name>/`).

## License

MIT
