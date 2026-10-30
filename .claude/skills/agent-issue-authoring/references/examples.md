# Examples and review moves

These examples are invented teaching cases. They are not claims about existing files,
approved requirements, real users, or observed test results.

## A progress log

"Add a workout log" leaves the interaction, stored fields, and preservation behavior
undefined. Ask whether the intended first result is recording a completed session,
displaying history, or something else. If recording is chosen, agree which information
is needed and where it belongs. A useful check might record two fictional sessions,
start a fresh agent session, and verify both records can be retrieved without changes.
Do not silently add a dashboard, accounts, or wearable integration.

## A supplied plan display

Separate the agent choosing exercises from the agent displaying an already supplied
plan. For the display issue, preserve the supplied exercises and source links, test
missing instructions, and inspect agreement between images and instructions. A local
web page is one possible delivery choice. It does not automatically have an agent
behind it, file access, a public URL, or a working backend.

## Research before implementation

If access to an external service is unknown, a build issue may be premature. Draft an
investigation that checks the documented access route, permissible data, and available
test environment, then delivers evidence and a recommendation. Agree an effort limit.
No access is a valid finding, not proof the integration works. Do not bypass restrictions
or insert credentials into the issue.

## Reorganize an existing website

Replace "make the code follow best practices" with an agreed structural change and
preservation criteria. Establish the existing pages and journeys to preserve; compare
before/after screenshots and actual behavior using the same inputs and viewports.
State which part of the structure may change and defer a redesign. This makes a real
maintenance issue rather than retroactively fabricating a development history.

## Several agents and overlapping issues

Identify the input/output boundary each issue owns, real prerequisites, and shared
files or interfaces. Link related work, suggest consolidation where outcomes duplicate,
and ask the author to resolve conflicting decisions. Do not merge, close, assign,
or implement issues solely because this authoring skill was loaded. Parallel work is
an option for the project owner, not a requirement of a good issue.
