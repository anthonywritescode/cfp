building pain-free python environments on macos at scale
========================================================

### description

In a world fraught with choices (brew / conda / macports / pip / easy_install /
venv / virtualenv / pyenv / python.org installers / macos python / etc.) how
does Lyft enable local and offline development of its 500+ python
micro-services?  This talk will detail the problems involved with scaling
local development tooling to thousands of developers with various (broken)
machine setups.  Along the way, this talk will cover many of the Open Source
technologies which made `lyftvenv` possible and how one could leverage some or
all of these tools to improve their own development environments.

### audience (who and why)

#### who is this talk for?

while this talk is primarily aimed at intermediate+ software developers, it
also contains helpful information and tools that are applicable to all
developers.  developers involved in infrastructure will likely get the most
out of this.

#### what background knowledge / experience is expected?

at the very least, it's expected that most will have experienced the _pain_
that it is to try and set up a consistent python environment on a mac or other
cross-platform situations.  it is helpful / expected that many have worked with
or have heard of virtual environments / python packaging / etc.

#### what do you expect the audience to do after this talk?

I expect the audience to learn some new useful tools that may be applicable
to their own workflows.  some of these tools may enable them to build more
efficient workflows at their own jobs, or to enable faster / more reliable
setups of their own machines.  they will be exposed to quite a few tools
which further this cause and will hopefully take away something about these.

### outline

#### introduction (before state, problem statements, etc.) (5 minutes)

- who am I?
- lyft's microservices at a high level
    - flask, pytest, hundreds of services, thousands of developers
    - piptools (requirements files) result in virtualenvs on linux in
      production (aws VMs, kubenetes pods, etc.)
- goals of a local development setup:
    - RED SQUIGGLIES! (making IDEs useful for development)
    - being able to iterate quickly with unit tests
    - work well with other tooling (linting, pre-commit, etc.)
    - make git pull work reliably
- before state:
    - bulky docker containers
    - slow unreliable remote execution
- python is a high level portable language... right? RIGHT?
    - xkcd:1987 (python environments)
    - binary dependencies, C extensions, and compilers OH MY
- macos is the wild wild west
    - no consistent package manager
    - too many ways to do everything (brew / ports / etc.)
    - can't really rely on much existing / working (especially in a
      post-catalina world)

#### enough sadness, how to make this work (20 minutes)

- deciding on a support matrix
    - what operating system versions are my developers using?
    - can I leverage IT to limit scope (require mojave+?)
    - graceful degredation for other platforms (design for the 90%+ but make it
      still kind-of work on arch/gentoo/fedora/whatever else the 1% wants to
      use)
- bootstrapping
    - how to go from (reliably) nothing working to a rock solid environment
    - no python, no (???) problem
    - distribute bootstrapping via `git` (automatic versioning / etc.)
    - prebuilding as much as possible
        - lyftvenv prebuilds pythons using brew
        - this is super fragile but the fragility is localized to the
          *builders* and not the *consumers*
- arch diagram
    - show the two loops (building prebuilt bundles vs. user installation)
- consistently provide correct settings
    - check for vpn setup
    - force installation from internal pypi
    - use the proper python version for the repository
- broken ssl?
    - for whatever reason, python ssl is often broken on macos?
    - bundle certifi fix script directly with lyftvenv
- pip install... wheels?
    - how does `pip install` usually work
    - what is a wheel?
    - delocate (how to prebuild wheels without worrying about binary deps)
    - cutting corners (shim packages when installation is basically impossible)
- building virtualenvs _faster_
    - `venv-update` / `pip-faster`: locally cache prebuilt wheels of things
      which are already installed.
- file watchers, immutability, and atomicity
    - don't ever give an IDE a partially built environment (sometimes it may
      never recover)
    - atomically update from one version of a virtualenv to another (lyftvenv
      uses symlink switching)
    - immutability of environments (don't let the user break the environment
      unless they explicitly ask for it)
        - disable `pip`, delete `easy_install`, etc.
        - `lyftvenv scratch` to get a mutable environment
        - `virtualenv-tools3` - make a copy of a virtualenv super fast while
          not breaking `.pyc` / `#!shebangs` / etc.
    - `fswatch` / `watchman` / etc. to watch requirements files to rebuild for
      changes
- self-healing environments
    - automatically detect broken virtualenvs and replace them
    - python version changes, OS version changes, etc. etc.

#### developer happiness (5 minutes)

- bundling tooling to make developer lives easier
    - `pre-commit` for linting / git hooks (lyftvenv will even automatically
      set up the hooks if you enable it)
    - `aactivator` - auto activation of virtualenvs
        - **probably the coolest thing one could take away**
        - comparable to `direnv` / etc. but with more of a focus on security
- don't do unnecessary things in critical path (updating / analytics / etc.)
- solid bug reporting
    - provide markdown / jira formatted bug reports on crashes
    - auto-detect common crashes and link documentation
    - version information up front
    - **copy paste everything including the comand you ran** as part of the
      error messaging
- automatic updating
    - fetch latest version in background
    - notify user update is available
    - force update in case of security / etc. issues
- "lyftvenv made me a better developer because it forced me to write self-
  contained unit tests"
- better mocks / fakes in unit tests
    - vcr / request replay / interface mocking
    - `pytest-env` - consistently set environment variables in tests
- distributing tools directly to developers
    - ability to replace clunky containerized solutions
