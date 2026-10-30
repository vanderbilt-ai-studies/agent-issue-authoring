"""Build the repository's student guide from the skill's canonical short guide."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
guide = ROOT / '.claude/skills/agent-issue-authoring/references/guide.md'
addition = '''

## Use the issue authoring skill

In Claude Desktop's Code tab, open your own project folder and ask:

> Use the agent-issue-authoring skill from https://github.com/vanderbilt-ai-studies/agent-issue-authoring to help me write or improve an issue for this project. Read my project context first.

The skill lives in [.claude/skills/agent-issue-authoring/](.claude/skills/agent-issue-authoring/SKILL.md).
Have your agent copy that complete folder into the appropriate skills directory
for your project. It includes its own guide, draft structure, and examples.
The folder follows the Agent Skills format; discovery and setup depend on the
agent application. The skill can also be loaded by its SKILL.md path.

It helps you draft, review, and split issues. It does not start implementing or
post issues merely because you asked for writing help. Tell it explicitly when
you want a reviewed issue saved on GitHub.

The [project-proposal helper](https://github.com/vanderbilt-ai-studies/project-proposal)
bundles this skill and calls it when you begin authoring issues. For an AI 1010
final project, you can draft issues before your consult, but implementation follows
the meeting and agreed plan. You do not need a finished backlog before the consult.

### Examples of requests

- "Help me turn this project requirement into the next useful issue."
- "Review this issue. Could a fresh agent carry it out and recognize success?"
- "These issues overlap. Help me separate their outcomes and dependencies."
- "I do not know whether the integration is possible. Help me write an investigation issue."

### Downloads and supporting material

- [One-page handout](docs/writing-an-agent-issue.pdf)
- [Editable Word handout](docs/writing-an-agent-issue.docx)
- [Adaptable issue structure](.claude/skills/agent-issue-authoring/references/issue-template.md)
- [Additional examples](.claude/skills/agent-issue-authoring/references/examples.md)
- [Sources and adaptations](docs/research-notes.md)

For maintainers, the short guide is canonical in the skill's references/guide.md.
Run `python3 scripts/build_readme.py` after editing it. When updating the bundled
copy in project-proposal, copy the complete skill folder and retain its reference
paths. Keep the student's solution files out of either helper repository.
'''
(ROOT/'README.md').write_text(guide.read_text().rstrip()+addition)
