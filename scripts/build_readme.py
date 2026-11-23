#!/usr/bin/env python3
"""Generate the catalog tables and skill count in README.md from skills.json.

Usage: python3 scripts/build_readme.py          # rewrite README.md
       python3 scripts/build_readme.py --check  # exit 1 if README.md is stale
"""
import json, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
GROUPS = ["Research", "Writing", "Orchestration", "Governance", "Engineering",
          "Safety and verification", "Hardware"]

RELATED = [
    ("multi-agent-orchestration-playbook", "Twelve rules for running teams of AI agents, an AGENTS.md template and tested helper scripts", "palimnote-agent-patterns"),
    ("ai-coding-agent-guardrail-hooks", "Tool-neutral guardrails CLI, Claude Code hook adapter and git hooks that block .env values and protected-path symlinks", "palimnote-tools"),
    ("local-first-llm-router", "Script, then local model, then cloud model, with privacy tiers and mechanical checks (Python library)", "palimnote-tools"),
    ("ollama-memory-governor", "Keep free RAM above a floor on a machine running several Ollama models (Python CLI or daemon)", "palimnote-tools"),
    ("safe-mcp-server-template", "Python template for an MCP server that treats tool output as untrusted", "palimnote-tools"),
    ("scholarly-citation-resolver", "Resolve a free-text citation to verified metadata from six open scholarly sources (TypeScript)", "palimnote-tools"),
    ("interactive-critical-edition", "Palimnote reader app: traceable critical editions from difficult scholarly texts (source-available, beta)", "app"),
]

INSTALL = [
    ("Claude Code", "`./install.sh --claude` (copies or links into `~/.claude/skills/<name>/`), or `--project <dir>` for `.claude/skills/`"),
    ("Codex", "`./install.sh --agents` (`.agents/skills/<name>/` in the project; `--user` for `~/.agents/skills`)"),
    ("Gemini CLI", "`./install.sh --agents` (Gemini CLI also scans `.agents/skills`), or `./install.sh --gemini` for a pointer block in `GEMINI.md`"),
    ("Cursor", "`./install.sh --agents` (`.agents/skills`), or `./install.sh --cursor` for a pointer block in `AGENTS.md`"),
    ("Copilot", "`./install.sh --copilot` adds a pointer block to `.github/copilot-instructions.md`; Copilot has no skills folder"),
    ("ChatGPT, Claude.ai, Gemini (chat)", "Paste the repo's `PROMPT.md` (or `SKILL.md` where there is no `PROMPT.md`) into the conversation"),
]

WORKS_WITH = """## Works with

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
"""

HOW_DIFFERS = """## How it differs

- [anthropics/skills](https://github.com/anthropics/skills) is Anthropic's own collection of skills and the reference for the SKILL.md format. This catalog does not replace it; it indexes separate, single-purpose repos (research, review, governance, safety) and keeps the same format so the skills load in the same places.
- Curated "awesome" lists of skills and prompts are large link lists. This one is small, generated from one `skills.json`, links only to repos by the same author, and says which surfaces were tested.
- Each skill is its own repo with its own `install.sh` (most also ship tests), not a folder inside a monorepo. That makes a single skill easy to clone and version, but it also means more repos to keep in sync.
- Most entries are for working on research and multi-agent projects. If you want general-purpose coding or document skills, look at the collections above first.
"""

def short(e):
    d = e["description"]
    return d if d.endswith(".") or len(d) < 400 else d

def build():
    skills = json.loads((ROOT / "skills.json").read_text())
    n = len(skills)
    planned = [e for e in skills if e.get("status") == "planned"]
    out = []
    out.append("# Palimnote Skills\n")
    out.append(f"Index of {n} portable `SKILL.md` agent skills and playbooks for research, writing, multi-agent review, governance and engineering. "
               "Each lives in its own repo and loads natively in Claude Code and Codex, or pastes into ChatGPT, Gemini, Cursor and Copilot."
               + (f" {len(planned)} of them are planned and have no public repo or `install.sh` yet; they are listed without links.\n" if planned else "\n"))
    out.append("The count and every table below are generated from [`skills.json`](skills.json) by `scripts/build_readme.py`. Edit the JSON, not the tables.\n")
    out.append("## Start here\n")
    for nm, txt in [("deep-research-skill", "Auditable literature and evidence review"),
                    ("hallucinated-citation-checker", "Check a bibliography for fabricated references"),
                    ("agent-report-evidence-gate", "Make an agent's \"done\" report show its evidence"),
                    ("release-privacy-scanner", "Scan a repo for leaks before a public push")]:
        e = next(x for x in skills if x["name"] == nm)
        out.append(f"- {txt}: " + (f"{nm} (planned, not yet published)" if e.get("status") == "planned" else f"[{nm}]({e['repo']})"))
    out.append("- Run a team of agents: [multi-agent-orchestration-playbook](https://github.com/hyderhusainarastu/multi-agent-orchestration-playbook)\n")
    out.append(WORKS_WITH)
    out.append(HOW_DIFFERS)
    out.append("## Install per tool\n")
    out.append("Every skill repo ships the same `install.sh`. Clone the repo you want, then:\n")
    out.append("| Tool | How |\n| --- | --- |")
    for t, h in INSTALL:
        out.append(f"| {t} | {h} |")
    out.append("\n`./install.sh --help` lists all targets, `--copy`, `--dry-run` and `--uninstall`. Each repo's README has its own capability table that says which surfaces were tested and which were not.\n")
    for g in GROUPS:
        rows = [e for e in skills if e["group"] == g]
        if not rows:
            continue
        out.append(f"## {g}\n")
        out.append("| Skill | What it does | Kind |\n| --- | --- | --- |")
        for e in rows:
            if e.get("status") == "planned":
                out.append(f"| {e['name']} (planned, not yet published) | {short(e)} | {e['kind']} |")
            else:
                out.append(f"| [{e['name']}]({e['repo']}) | {short(e)} | {e['kind']} |")
        out.append("")
    out.append("## Related repos (no SKILL.md)\n")
    out.append("These ship tools, libraries or patterns rather than a skill. They are listed here so the skills above link to them; each is indexed in its own catalog.\n")
    out.append("| Repo | What it does | Catalog |\n| --- | --- | --- |")
    for name, what, cat in RELATED:
        c = f"[{cat}](https://github.com/hyderhusainarastu/{cat})" if cat != "app" else "app"
        out.append(f"| [{name}](https://github.com/hyderhusainarastu/{name}) | {what} | {c} |")
    out.append("")
    out.append("## Link check\n")
    out.append("`python3 scripts/check_links.py` checks that every GitHub link in this README answers with HTTP 200 (needs network). `python3 scripts/check_links.py --list` prints the links without fetching.\n")
    out.append("## License\n")
    out.append("MIT\n")
    out.append("---\n")
    out.append("Part of the Palimnote catalogs: [palimnote-skills](https://github.com/hyderhusainarastu/palimnote-skills), "
               "[palimnote-tools](https://github.com/hyderhusainarastu/palimnote-tools), "
               "[palimnote-templates](https://github.com/hyderhusainarastu/palimnote-templates), "
               "[palimnote-agent-patterns](https://github.com/hyderhusainarastu/palimnote-agent-patterns). "
               "More at https://github.com/hyderhusainarastu\n")
    return "\n".join(out)

if __name__ == "__main__":
    text = build()
    p = ROOT / "README.md"
    if "--check" in sys.argv:
        sys.exit(0 if p.read_text() == text else 1)
    p.write_text(text)
