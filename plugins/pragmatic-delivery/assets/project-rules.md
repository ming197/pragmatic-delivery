<!-- pragmatic-delivery:start -->
## Pragmatic Delivery

Default to an 80/20 fast-delivery path for ordinary software changes.

- Start from the requested outcome and acceptance criteria. Infer ordinary reversible details from repository conventions.
- Inspect only enough code to identify the affected path and existing pattern.
- Implement the smallest end-to-end change that satisfies the current request.
- Do not add speculative features, abstractions, configuration, fallbacks, dependencies, or future-proofing.
- Do not refactor, rename, reformat, document, or fix unrelated code.
- Tolerate small duplication until a stable recurring pattern exists.
- Do not create a proposal, specification, design document, or detailed plan for a clear local change.

Handle an edge case only when it is likely in normal use, required by the request, covered by surrounding behavior, needed to prevent a regression, or capable of high-impact harm. High-impact harm includes security or privacy exposure, authorization failure, financial loss, irreversible data loss, public compatibility breakage, and unsafe operations. Do not implement defenses for merely imaginable low-probability, low-impact scenarios.

Verify proportionately: the main success path, the most common relevant failure path, affected regressions, and applicable high-impact boundaries. Do not create exhaustive test matrices for speculative combinations.

Use the installed `planning-first` skill only when material ambiguity, cross-module design, migration, public compatibility, consequential architectural tradeoffs, or major scope expansion makes direct implementation unsafe. Planning must remain short and must end once the blocking decisions are resolved.

Use the installed `pragmatic-security-review` skill only for authentication, authorization, secrets, untrusted input, privacy, payment, destructive operations, or an explicit security review. Do not turn ordinary changes into general security audits.

Stop when requested behavior works, relevant checks pass, the diff is scoped, and important limitations are stated. Report concrete verification evidence instead of pursuing unrequested completeness.
<!-- pragmatic-delivery:end -->
