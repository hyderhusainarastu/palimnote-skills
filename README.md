# Palimnote Skills

Index of 30 portable `SKILL.md` agent skills and playbooks for research, writing, multi-agent review, governance and engineering. Each lives in its own repo and loads natively in Claude Code and Codex, or pastes into ChatGPT, Gemini, Cursor and Copilot.

The count and every table below are generated from [`skills.json`](skills.json) by `scripts/build_readme.py`. Edit the JSON, not the tables.

## Start here

- Auditable literature and evidence review: [deep-research-skill](https://github.com/hyderhusainarastu/deep-research-skill)
- Check a bibliography for fabricated references: [hallucinated-citation-checker](https://github.com/hyderhusainarastu/hallucinated-citation-checker)
- Make an agent's "done" report show its evidence: [agent-report-evidence-gate](https://github.com/hyderhusainarastu/agent-report-evidence-gate)
- Scan a repo for leaks before a public push: [release-privacy-scanner](https://github.com/hyderhusainarastu/release-privacy-scanner)
- Run a team of agents: [multi-agent-orchestration-playbook](https://github.com/hyderhusainarastu/multi-agent-orchestration-playbook)

## Works with

This table is about this catalog repo (`skills.json`, the generator and the tests), not about each skill; every skill repo has its own capability table.

| Surface | How | Status |
| --- | --- | --- |
| Any shell, CI | `python3 -m unittest discover -s tests` and `python3 scripts/build_readme.py --check` (stdlib only) | tested 2026-11-23, Python 3.14, macOS; also run by `.github/workflows/ci.yml` on push |
| Any tool that can read JSON | read `skills.json` for names, kinds, topics and install commands | tested (schema checked by the unit tests); no agent was asked to use it |
| Claude Code | clone a skill repo, `./install.sh --claude` | documented, not tested from this catalog |
| Codex | `./install.sh --agents` | documented, not tested from this catalog |
| Gemini CLI | `./install.sh --agents` or `--gemini` | documented, not tested from this catalog |
| Cursor | `./install.sh --agents` or `--cursor`; reads `AGENTS.md` | documented, not tested from this catalog |
| Copilot | `./install.sh --copilot` (pointer block) | documented, not tested from this catalog |
| ChatGPT, Claude.ai, Gemini (chat) | paste the skill repo's `PROMPT.md` | documented, not tested from this catalog |

## Example

List the skills in one group straight from the index:

```sh
$ python3 -c "import json; [print(e['name'], '|', e['kind']) for e in json.load(open('skills.json')) if e['group'] == 'Safety and verification']"
agent-report-evidence-gate | skill
release-privacy-scanner | skill
```

Then install one with its own repo, for example `git clone https://github.com/hyderhusainarastu/release-privacy-scanner && cd release-privacy-scanner && ./install.sh --claude --dry-run`.

## How it differs

- [anthropics/skills](https://github.com/anthropics/skills) is Anthropic's own collection of skills and the reference for the SKILL.md format. This catalog does not replace it; it indexes separate, single-purpose repos (research, review, governance, safety) and keeps the same format so the skills load in the same places.
- Curated "awesome" lists of skills and prompts are large link lists. This one is small, generated from one `skills.json`, links only to repos by the same author, and says which surfaces were tested.
- Each skill is its own repo with its own `install.sh` (most also ship tests), not a folder inside a monorepo. That makes a single skill easy to clone and version, but it also means more repos to keep in sync.
- Most entries are for working on research and multi-agent projects. If you want general-purpose coding or document skills, look at the collections above first.

## Install per tool

Every skill repo ships the same `install.sh`. Clone the repo you want, then:

| Tool | How |
| --- | --- |
| Claude Code | `./install.sh --claude` (copies or links into `~/.claude/skills/<name>/`), or `--project <dir>` for `.claude/skills/` |
| Codex | `./install.sh --agents` (`.agents/skills/<name>/` in the project; `--user` for `~/.agents/skills`) |
| Gemini CLI | `./install.sh --agents` (Gemini CLI also scans `.agents/skills`), or `./install.sh --gemini` for a pointer block in `GEMINI.md` |
| Cursor | `./install.sh --agents` (`.agents/skills`), or `./install.sh --cursor` for a pointer block in `AGENTS.md` |
| Copilot | `./install.sh --copilot` adds a pointer block to `.github/copilot-instructions.md`; Copilot has no skills folder |
| ChatGPT, Claude.ai, Gemini (chat) | Paste the repo's `PROMPT.md` (or `SKILL.md` where there is no `PROMPT.md`) into the conversation |

`./install.sh --help` lists all targets, `--copy`, `--dry-run` and `--uninstall`. Each repo's README has its own capability table that says which surfaces were tested and which were not.

## Research

| Skill | What it does | Kind |
| --- | --- | --- |
| [quote-verification-toolkit](https://github.com/hyderhusainarastu/quote-verification-toolkit) | Verify quoted excerpts against source texts, tolerant of PDF line-wraps, Unicode punctuation, and elision | skill |
| [source-intake-pipeline](https://github.com/hyderhusainarastu/source-intake-pipeline) | Gated intake pipeline for research sources: metadata verification, citability classification, dedupe, provenance | skill |
| [citation-lead-mining-and-dedup](https://github.com/hyderhusainarastu/citation-lead-mining-and-dedup) | Mine candidate references and idea leads from source text into deduplicated follow-up tables | skill |
| [source-authority-hierarchy](https://github.com/hyderhusainarastu/source-authority-hierarchy) | A tiered authority hierarchy for resolving conflicts between sources when evidence disagrees | playbook |
| [empirical-study-design-and-gold-set-toolkit](https://github.com/hyderhusainarastu/empirical-study-design-and-gold-set-toolkit) | Design empirical evaluations end to end and build gold-standard sets with blinding and leakage controls | skill |
| [scholarly-metadata-resolution-pattern](https://github.com/hyderhusainarastu/scholarly-metadata-resolution-pattern) | Resolve bibliographic metadata across Crossref, OpenAlex, Google Books, and Open Library with fallback ordering | playbook |
| [deep-research-skill](https://github.com/hyderhusainarastu/deep-research-skill) | Research you can audit: saturation stop rule, explicit verification levels and bounded negative findings, run by parallel agents or by one chat in sequence. Includes CSV schemas and a corpus keyword audit script. | skill |
| [hallucinated-citation-checker](https://github.com/hyderhusainarastu/hallucinated-citation-checker) | Check every BibTeX entry against Crossref, OpenAlex, arXiv, Open Library and doi.org to catch fabricated or garbled references; CSV verdict per key. Also a Python CLI (primary listing in palimnote-tools). | skill |
| [gated-research-pipeline](https://github.com/hyderhusainarastu/gated-research-pipeline) | Template for AI-assisted research writing: every claim traces to a checkable source and nothing is done until it clears a readiness gate. Ships four skills, ledgers and provenance tools. | skill |

## Writing

| Skill | What it does | Kind |
| --- | --- | --- |
| [ai-writing-humanizer](https://github.com/hyderhusainarastu/ai-writing-humanizer) | Detect AI-sounding patterns in prose and rewrite in an authentic human voice, with channel-specific rules (adapted from a community skill) | skill |
| [author-style-profile-mining](https://github.com/hyderhusainarastu/author-style-profile-mining) | Mine a writing corpus for an author's stylistic tics and turn them into imitation or avoidance rules | skill |
| [structural-checklist-from-exemplars](https://github.com/hyderhusainarastu/structural-checklist-from-exemplars) | Derive a reusable structural checklist for any document genre by comparing exemplar documents | skill |
| [manuscript-mechanical-qa-sweep-pipeline](https://github.com/hyderhusainarastu/manuscript-mechanical-qa-sweep-pipeline) | Mechanical pre-review QA sweeps for long-form manuscripts: leak greps, claim-verb discipline, compile gate | skill |
| [pre-submission-manuscript-audit](https://github.com/hyderhusainarastu/pre-submission-manuscript-audit) | Full-manuscript, analysis-only pre-submission audit: argument structure, venue fit, literature gaps, novelty threats, citation accuracy, reviewer simulation | skill |

## Orchestration

| Skill | What it does | Kind |
| --- | --- | --- |
| [gated-multi-agent-review-lifecycle](https://github.com/hyderhusainarastu/gated-multi-agent-review-lifecycle) | A gate lifecycle for multi-agent work: structured verdicts, failure routing, escalation, no self-approval | playbook |
| [agent-brief-schema-for-specialist-roles](https://github.com/hyderhusainarastu/agent-brief-schema-for-specialist-roles) | A fixed briefing schema for specialist agents: scope, inputs, tools, output contract, acceptance tests | playbook |
| [adversarial-peer-review-role](https://github.com/hyderhusainarastu/adversarial-peer-review-role) | An adversarial reviewer role: severity taxonomy, evidence citations, disconfirmation duty | playbook |
| [cross-model-second-opinion](https://github.com/hyderhusainarastu/cross-model-second-opinion) | Get a budgeted second opinion from a different AI model: when to ask, read-only and ephemeral CLI recipes, a call cap, and how to weigh the answer. | skill |

## Governance

| Skill | What it does | Kind |
| --- | --- | --- |
| [legacy-plan-reconciliation-matrix](https://github.com/hyderhusainarastu/legacy-plan-reconciliation-matrix) | Audit an outdated plan against current evidence with a REUSE, REVISE, REJECT, DEFER, VERIFY matrix | playbook |
| [governance-records-ledger-conventions](https://github.com/hyderhusainarastu/governance-records-ledger-conventions) | Append-only conventions for decision logs, task ledgers, and open-question files in long-running projects | playbook |
| [evidence-ledger-and-phase-handoff-convention](https://github.com/hyderhusainarastu/evidence-ledger-and-phase-handoff-convention) | Evidence ledgers and phase-handoff documents that pass auditable context between sessions or agents | playbook |
| [pre-publication-review-gate-checklist](https://github.com/hyderhusainarastu/pre-publication-review-gate-checklist) | Pre-launch review gate: claim accuracy, accessibility, privacy, and synthetic demo-data disclosure | playbook |
| [ai-project-cost-modeling](https://github.com/hyderhusainarastu/ai-project-cost-modeling) | A structured cost model for AI-assisted projects: category taxonomy across low, base, and high scenarios | playbook |

## Engineering

| Skill | What it does | Kind |
| --- | --- | --- |
| [llm-routing-and-judge-eval-harness-pattern](https://github.com/hyderhusainarastu/llm-routing-and-judge-eval-harness-pattern) | Provider-agnostic LLM routing with deterministic fallback, plus an LLM-as-judge eval harness with gold sets | playbook |
| [accessible-dialog-focus-trap-primitives](https://github.com/hyderhusainarastu/accessible-dialog-focus-trap-primitives) | Accessible React dialog primitives: focus trap, escape handling, focus restoration, live-region announcements | skill |
| [nextjs-cloudflare-workers-landing-site-setup](https://github.com/hyderhusainarastu/nextjs-cloudflare-workers-landing-site-setup) | Wire a Next.js landing site onto Cloudflare Workers with wrangler and Drizzle, from scratch | skill |
| [context-window-text-chunking](https://github.com/hyderhusainarastu/context-window-text-chunking) | Paragraph-boundary-aware text chunking for fitting long documents into LLM context windows | skill |

## Safety and verification

| Skill | What it does | Kind |
| --- | --- | --- |
| [agent-report-evidence-gate](https://github.com/hyderhusainarastu/agent-report-evidence-gate) | CLI plus skill that checks an agent's "done" report for evidence completeness: cited files exist, success claims sit next to evidence, structured claims re-verify. Primary listing in palimnote-tools. | skill |
| [release-privacy-scanner](https://github.com/hyderhusainarastu/release-privacy-scanner) | Scan a repo, its git history and release archives for local paths, personal identifiers, emails, hostnames and secret-shaped strings before a public push or double-blind submission. Primary listing in palimnote-tools. | skill |

## Hardware

| Skill | What it does | Kind |
| --- | --- | --- |
| [hardware-mod-toolkit](https://github.com/hyderhusainarastu/hardware-mod-toolkit) | Skills for reverse engineering and modding consumer hardware: serial and USB recon, firmware image analysis, framed serial protocols, safe MCU backup, hardware-in-the-loop testing and publish hygiene. | skill |

## Related repos (no SKILL.md)

These ship tools, libraries or patterns rather than a skill. They are listed here so the skills above link to them; each is indexed in its own catalog.

| Repo | What it does | Catalog |
| --- | --- | --- |
| [multi-agent-orchestration-playbook](https://github.com/hyderhusainarastu/multi-agent-orchestration-playbook) | Twelve rules for running teams of AI agents, an AGENTS.md template and tested helper scripts | [palimnote-agent-patterns](https://github.com/hyderhusainarastu/palimnote-agent-patterns) |
| [ai-coding-agent-guardrail-hooks](https://github.com/hyderhusainarastu/ai-coding-agent-guardrail-hooks) | Tool-neutral guardrails CLI, Claude Code hook adapter and git hooks that block .env values and protected-path symlinks | [palimnote-tools](https://github.com/hyderhusainarastu/palimnote-tools) |
| [local-first-llm-router](https://github.com/hyderhusainarastu/local-first-llm-router) | Script, then local model, then cloud model, with privacy tiers and mechanical checks (Python library) | [palimnote-tools](https://github.com/hyderhusainarastu/palimnote-tools) |
| [ollama-memory-governor](https://github.com/hyderhusainarastu/ollama-memory-governor) | Keep free RAM above a floor on a machine running several Ollama models (Python CLI or daemon) | [palimnote-tools](https://github.com/hyderhusainarastu/palimnote-tools) |
| [safe-mcp-server-template](https://github.com/hyderhusainarastu/safe-mcp-server-template) | Python template for an MCP server that treats tool output as untrusted | [palimnote-tools](https://github.com/hyderhusainarastu/palimnote-tools) |
| [scholarly-citation-resolver](https://github.com/hyderhusainarastu/scholarly-citation-resolver) | Resolve a free-text citation to verified metadata from six open scholarly sources (TypeScript) | [palimnote-tools](https://github.com/hyderhusainarastu/palimnote-tools) |
| [interactive-critical-edition](https://github.com/hyderhusainarastu/interactive-critical-edition) | Palimnote reader app: traceable critical editions from difficult scholarly texts (source-available, beta) | app |

## Link check

`python3 scripts/check_links.py` checks that every GitHub link in this README answers with HTTP 200 (needs network). `python3 scripts/check_links.py --list` prints the links without fetching.

## License

MIT

---

Part of the Palimnote catalogs: [palimnote-skills](https://github.com/hyderhusainarastu/palimnote-skills), [palimnote-tools](https://github.com/hyderhusainarastu/palimnote-tools), [palimnote-templates](https://github.com/hyderhusainarastu/palimnote-templates), [palimnote-agent-patterns](https://github.com/hyderhusainarastu/palimnote-agent-patterns). More at https://github.com/hyderhusainarastu
