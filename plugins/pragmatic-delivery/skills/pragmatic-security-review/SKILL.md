---
name: pragmatic-security-review
description: Review the high-impact security boundaries of a software change without speculative hardening. Use for authentication, authorization, secrets, untrusted input, privacy, payment, destructive operations, or explicit security-review requests; do not invoke for ordinary low-risk changes.
---

# Pragmatic Security Review

Review only the security boundary introduced or affected by the current change.

- Trace entry points, trust boundaries, sensitive data, authorization decisions, and irreversible effects.
- Prioritize exploitable or high-impact failures supported by code or a realistic path. Do not report theoretical issues without a plausible trigger and consequence.
- Check the primary abuse path plus existing security regressions. Reuse repository security controls instead of introducing a parallel framework.
- Preserve mandatory validation, authorization, audit, secret handling, and data-safety protections even when simplifying code.
- Classify findings as blocking or follow-up. A blocking finding must plausibly enable unauthorized access, data exposure or loss, financial harm, code execution, or a destructive action.

Return concise findings with evidence, impact, and the smallest remediation. If no blocking issue exists, say so and allow delivery to continue. Do not expand into a general security audit unless requested.
