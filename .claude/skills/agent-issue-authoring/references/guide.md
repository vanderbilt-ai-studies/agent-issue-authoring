# Write an issue that steers an AI agent

A GitHub issue is a written job for the artificial intelligence (AI) agent helping you develop a solution. Give it one useful outcome, the context needed to act, and a way to recognize success. You can ask AI to help write the issue; you supply the purpose and judge the result.

## Begin with one useful outcome

Name what should change and who benefits. "Show the supplied workout plan on a readable page" gives direction. "Build my exercise app" leaves too many decisions open. Choose a piece you can try and review on its own. It can involve software, a skill, research, or another part of your solution.

## Give the agent the context it needs

Link the relevant part of your specification, existing files, and earlier decisions. State the starting input and expected output. Check that referenced files exist and that required access works. Name unfinished dependencies. If the approach is uncertain, write a research issue with a question, a bounded investigation, and a decision or evidence report to deliver. You do not need to invent technical details to sound precise.

## Define success with an observable check

Acceptance criteria describe what must be true for you to accept the work. Replace "make it good" with a starting situation, an action, and an expected result. Include a realistic failure case. A test can be an automated check, a trial of the actual skill, a browser walkthrough, or a documented human review. Explain how you will judge quality where a mechanical check is insufficient.

## Set the scope and stopping conditions

Say what belongs in this issue and what should wait. "Use only the supplied exercises; do not generate a new plan" limits the work. "Use only this folder" limits access; it does not define the job. Let the agent choose ordinary implementation details unless a real constraint matters. Stop when the checks pass, an agreed time or usage limit is reached, or a missing decision or dependency blocks progress. Written instructions complement tool permissions; they do not enforce them.

## Example adapted from Thursday

**Title:** Display a supplied workout plan on a readable web page

**Goal and context:** Let someone follow an already approved plan. Read the project's display requirements and supplied example plan. Identify their actual paths before work begins; if the plan is missing, report the dependency.

**Done when:** Every supplied exercise appears once with its name, instructions, and agreed amount. Each exercise has a labeled illustration that agrees with the instructions. Supplied source links remain accessible. At phone width, the page has no horizontal scrolling. Missing instructions are flagged rather than invented.

**Scope and checks:** Build the display and a short usage guide. Leave exercise selection, accounts, wearables, and hosting for later. Try a complete fictional plan and one missing instructions; compare the page with each input and review the illustrations. Stop and report any unresolved mismatch.

## Review before you delegate

Could an agent starting a fresh session tell what to read, what to do, and how to check it? After the work, inspect the actual result and evidence. Revise and retest where needed. Link reviewed changes to the issue; GitHub closes an issue from a `Closes #N` commit when that commit reaches the default branch. Keep unresolved work visible.

**Sources:** [GitHub guidance](https://docs.github.com/en/copilot/tutorials/cloud-agent/get-the-best-results), [Sayagh's observational study](https://arxiv.org/abs/2512.21426), and [GitHub closing keywords](https://docs.github.com/en/issues/tracking-your-work-with-issues/using-issues/linking-a-pull-request-to-an-issue). Adapted from AI 1010, October 29, 2026. These are practical guidelines, not a guarantee of success.
