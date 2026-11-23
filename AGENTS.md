# Agent instructions

## Using this catalog
- `skills.json` is the index of skill repos. Read it to find a skill by name, kind, topics and install commands.
- Install a skill by cloning its repo and running its `install.sh` (`--claude`, `--agents`, `--gemini`, `--cursor`, `--copilot`). Run `./install.sh --help` first and prefer `--dry-run`.
- For chat tools without a skills folder, paste the repo's `PROMPT.md`.
- Never claim a platform works unless that repo's capability table says it was tested.

## Working on this repo
- Edit `skills.json`, then run `python3 scripts/build_readme.py`. Do not edit the README tables by hand.
- Test: `python3 -m unittest discover -s tests` (offline).
- Link check: `python3 scripts/check_links.py` (network). `--list` prints links offline.
- Keep the skill count generated; never hard-code it.
- No `.claude-plugin/marketplace.json`: its schema was not verified against current docs.
- Do not add secrets, local paths or personal data.
