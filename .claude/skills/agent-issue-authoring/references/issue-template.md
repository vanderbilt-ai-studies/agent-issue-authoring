# Issue draft structure

Use only the fields that help this issue. Respect an existing project template.

```markdown
Title: [Specific outcome or observed problem]

## Goal
Who needs what change, and why does it matter in the larger solution?

## Context and inputs
Relevant specification criteria, actual files/source links, starting state,
expected output, decisions already made, and dependencies still missing.

## Acceptance criteria and checks
- [ ] Given [starting state], when [action], [observable expected result].
      Check: [actual command or procedure and what to observe].
- [ ] Given [meaningful failure case], [intended response].
      Check: [how to inspect it, including any human judgment].

## Scope and limits
Included work:
Deferred work:
Real constraints on methods, access, data, and sources:
Stop when checks pass, the agreed resource limit is reached, or [specific blocker].

## Evidence for review
Changed files or artifact, actual checks/results, and remaining limits.
```

For a bug, add reproducible steps, expected versus observed behavior, environment,
and available evidence. For research, specify the question, investigation boundary,
and the report or decision that would complete the issue. Avoid filling unknowns
with generic promises such as "follow best practices" or "handle all edge cases."
