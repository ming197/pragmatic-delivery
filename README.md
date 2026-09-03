# Pragmatic Delivery

A lightweight, risk-adaptive delivery plugin for Codex and Claude Code. It optimizes for a useful result quickly instead of making every change pass through a specification ceremony.

## How it works

- **Default path — 80/20 delivery:** understand the objective, inspect the relevant code, implement the smallest complete vertical slice, verify it proportionately, and stop.
- **Planning First:** used only when material uncertainty, cross-module coordination, migration risk, or a public contract makes direct implementation unsafe.
- **Pragmatic Security Review:** used only for meaningful security boundaries such as authentication, authorization, secrets, untrusted input, sensitive data, payments, or destructive operations.

The default project rules explicitly avoid speculative abstractions, exhaustive unlikely edge cases, and documentation that does not help ship the current objective.

## Install in Codex

```text
codex plugin marketplace add ming197/pragmatic-delivery
codex plugin add pragmatic-delivery@pragmatic-delivery-kit
```

Then ask Codex to run `$setup-delivery-rules`. It adds a managed block to `AGENTS.md` and `CLAUDE.md` without replacing existing project instructions.

## Install in Claude Code

```text
/plugin marketplace add ming197/pragmatic-delivery
/plugin install pragmatic-delivery@pragmatic-delivery-kit
```

Then run `/pragmatic-delivery:setup-delivery-rules`.

## Skills

| Skill | Trigger | Purpose |
| --- | --- | --- |
| `setup-delivery-rules` | Explicit only | Install or refresh project-level rules |
| `planning-first` | Complex or materially uncertain work | Produce a short, decision-oriented plan |
| `pragmatic-security-review` | High-risk work | Check plausible, high-impact security failures |

## Manual rules installation

From the plugin directory:

```bash
python3 scripts/install_project_rules.py --project /path/to/project --target both
```

The installer is idempotent and preserves content outside its marked block. Use `--check` to preview whether files need updating.

## Philosophy

The goal is not careless speed. It is deliberate proportionality: spend engineering effort where failure is likely or expensive, and keep ordinary product work moving through small vertical slices, trunk-based integration, and continuous delivery.

## License

MIT
