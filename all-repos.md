Making microservices feel like monoliths
========================================

### description

As a technical organization scales, moving from a single-repository monolith
to microservices may be a good strategy to maintain agility but at what cost?
This talk describes some of the difficulties of moving to many repos and
introduces a tool (all-repos) which provides distributed discoverability and
refactoring tooling.

### detailed abstract

Part 1: Describing challenges organizations face while scaling number of
developers in a single repository
- ownership
- ease / speed of deployment
- version control issues: conflicts / tooling speed, etc.

Part 2: some of the reasons microservices / many repositories solve these
issues
- ownership: individual repositories owned by teams (but potentially a
  double-edged sword!)
- ease / speed of deployment: individual repositories can be deployed
  independently and usually more quickly since they are smaller
- version control issues: with many repositories, conflicts are less common as
  individuals work in their own codebases.  There also aren't problems of the
  version control system scaling to the codebase (google / facebook building
  their own VCS solutions to work around this).

Part 3: Some of the problems introduced by microservices
- Difficult to find code / traverse boundaries
- Drift in project setup / best practices
- Quite the tedious process to upgrade dependencies / fix security issues / etc.

Part 4: Introducing all-repos
- all-repos is a tool which makes it easy to clone all available repositories
- composable tooling for common discoverability and searching tooling
- tooling to write automated refactor procedures to apply across all codebases
- pluggable source / push modules to customize for your VCS setup

Part 5: Showing some examples using all-repos
- quick-and-dirty `all-repos-sed` to do some string replacement
- more in-depth fixer
- integration with `pre-commit` / using `pre-commit` as a tool for enforcing
  consistency across codebases

### what attendees will learn

- some of the organizational reasons for moving to microservices
- challenges faced in many-repository microservices
- how all-repos can help with discoverability and refactoring in a
  many-repository setup

