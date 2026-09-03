---
name: setup-delivery-rules
description: Install or refresh the Pragmatic Delivery managed rule block in a project's AGENTS.md and CLAUDE.md. Use only when the user explicitly asks to set up, enable, install, or update the plugin's project rules.
---

# Set Up Delivery Rules

Run the plugin's installer from the target project root:

```bash
python3 <plugin-root>/scripts/install_project_rules.py --target both
```

On Claude Code, `<plugin-root>` is available as `${CLAUDE_PLUGIN_ROOT}`. On Codex, locate `scripts/install_project_rules.py` from the installed Skill directory and run it directly.

The installer owns only the text between its managed markers. Preserve all other project instructions. Report which files were created, updated, or already current.
