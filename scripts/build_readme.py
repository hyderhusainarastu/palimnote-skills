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

def short(e):
    d = e["description"]
    return d if d.endswith(".") or len(d) < 400 else d

def build():
    skills = json.loads((ROOT / "skills.json").read_text())
    n = len(skills)
    out = []
    out.append("# Palimnote Skills\n")
    out.append(f"Index of {n} portable `SKILL.md` agent skills and playbooks for research, writing, multi-agent review, governance and engineering. "
               "Each lives in its own repo and loads natively in Claude Code and Codex, or pastes into ChatGPT, Gemini, Cursor and Copilot.\n")
    out.append("The count and every table below are generated from [`skills.json`](skills.json) by `scripts/build_readme.py`. Edit the JSON, not the tables.\n")
    out.append("## Start here\n")
    out.append("- Auditable literature and evidence review: [deep-research-skill](https://github.com/hyderhusainarastu/deep-research-skill)")
    out.append("- Check a bibliography for fabricated references: [hallucinated-citation-checker](https://github.com/hyderhusainarastu/hallucinated-citation-checker)")
    out.append("- Make an agent's \"done\" report show its evidence: [agent-report-evidence-gate](https://github.com/hyderhusainarastu/agent-report-evidence-gate)")
    out.append("- Scan a repo for leaks before a public push: [release-privacy-scanner](https://github.com/hyderhusainarastu/release-privacy-scanner)")
    out.append("- Run a team of agents: [multi-agent-orchestration-playbook](https://github.com/hyderhusainarastu/multi-agent-orchestration-playbook)\n")
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
