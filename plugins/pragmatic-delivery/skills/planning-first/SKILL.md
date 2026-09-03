---
name: planning-first
description: Resolve material implementation uncertainty with a short, codebase-grounded plan before coding. Use for cross-module changes, migrations, public contracts, consequential design tradeoffs, or scope that cannot safely proceed by following an existing pattern; do not use for clear local changes.
---

# Planning First

Resolve only the uncertainty that could materially change implementation.

1. Restate the outcome and non-negotiable constraints briefly.
2. Inspect the smallest relevant portion of the repository, including existing patterns and affected tests.
3. Identify the decisions that would change behavior, compatibility, data, operations, or rollback. Ignore naming and other reversible details.
4. Compare at most two credible approaches. Recommend one using simplicity, reversibility, repository fit, and delivery time.
5. Define the first end-to-end implementation slice and how it will be verified and rolled back.

Keep the result concise and in the conversation. Do not create a PRD, RFC, specification, task hierarchy, or durable plan file unless the user requests one.

If investigation shows the change is straightforward, end planning immediately and proceed through the normal fast path. Ask the user only for a decision that cannot be safely inferred. After that decision, continue implementation rather than restarting planning.
