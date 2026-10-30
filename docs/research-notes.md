# Evidence and design choices

Reviewed October 30, 2026. This guide is an original teaching synthesis of Jesse
Spencer-Smith's October 29 AI 1010 classes, the course project workflow, and the
primary sources below. External skills were inspected as examples, not installed
or adopted as instructions for this project.

## Research and official documentation

- [GitHub, Best practices for using GitHub Copilot to work on tasks](https://docs.github.com/en/copilot/tutorials/cloud-agent/get-the-best-results).
  Supports clear problem descriptions, acceptance criteria, useful repository
  context, and a working validation environment. We apply the authoring principles
  across development agents without claiming identical behavior across products.
- [Mohammed Sayagh, What Makes a GitHub Issue Ready for Copilot?](https://arxiv.org/abs/2512.21426)
  (2025), arXiv preprint. The study examines issue characteristics associated with
  merged versus closed pull requests. Its findings favor concise, bounded work
  with useful guidance. This is observational evidence about a particular setting,
  not a causal guarantee. The association involving external dependencies is not
  a reason to remove necessary source links; instead, verify dependencies and
  summarize what the agent needs to know. We do not turn its criteria into a
  student grading scale or a universal readiness score.
- [GitHub, Linking a pull request to an issue](https://docs.github.com/en/issues/tracking-your-work-with-issues/using-issues/linking-a-pull-request-to-an-issue).
  Verifies the default-branch behavior of closing keywords in commit messages.

## Existing authored skills inspected

- [GitHub Awesome Copilot, github-issues](https://github.com/github/awesome-copilot/blob/main/skills/github-issues/SKILL.md).
  Useful repository-context checks, issue templates, and preservation of unrelated
  fields when updating. Its broader issue-management operations are outside the
  default scope of this authoring helper. Tool names in that source are not assumed
  to exist in another environment.
- [GitHub Awesome Copilot, create-github-issues-feature-from-implementation-plan](https://github.com/github/awesome-copilot/blob/main/skills/create-github-issues-feature-from-implementation-plan/SKILL.md).
  Useful traceability from a plan to issues and a duplicate check. We do not require
  one issue per phase: a large phase can contain several independently reviewable
  outcomes, and preparation may belong with the capability it supports.
- [Jesse Vincent, Superpowers writing-plans](https://github.com/obra/superpowers/blob/main/skills/writing-plans/SKILL.md).
  Useful attention to the context a fresh implementer lacks and deliverables with
  observable checks. We adapt the principle without requiring a software stack,
  a particular test-development sequence, or a detailed implementation script for
  every student issue. The issue can specify the outcome while leaving ordinary
  technical choices to the agent.

## Course grounding

- AI 1010, October 29, section 01: bounded issues at 33:28-35:45; student exercise
  and discussion at 57:05-73:18; issue prioritization at 73:24-79:59.
- Section 02: success and stopping conditions at 19:18-21:45; scope versus access
  at 58:56-60:54; an issue-authoring helper at 61:48-63:31; dependencies at
  63:36-68:13; concrete scope and tests at 69:09-75:56; closing commits at
  78:13-80:11.
- [Project proposal helper](https://github.com/vanderbilt-ai-studies/project-proposal)
  and [Career Services repository process](https://github.com/vanderbilt-ai-studies/career-services-project/blob/main/docs/repository-process.md).
  Preserve the student's ambition, specification, decisions, meaningful checks,
  and actual evidence. For AI 1010 final projects, implementation follows the
  instructor consult and agreed plan; issue drafts need not delay that consult.

The example is newly written from the classroom scenario. It does not reproduce
student issue text or identify students. Research on issue quality does not
establish medical claims about exercise, so the guide treats the workout plan
as supplied content and makes no exercise prescription.
