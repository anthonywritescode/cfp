# lazy imports: how they work and why you should(n't) use them

## abstract

PEP 810 brings a new `lazy` import to python 3.15

This talk will deep dive into how they work, the three main uses, and some
best practices + gotchas.

## supplemental information

30 minute talk ideally, can be 45 (possible also future-lazy-imports).

notes / outline: https://github.com/anthonywritescode/cfp/blob/main/lazy-imports.md

previous presentations (parts of these are combined into this talk):

- lazy imports: https://www.youtube.com/watch?v=xnZ90CYYF-0
- backporting lazy imports: https://www.youtube.com/watch?v=mQY5UR78t9g
    - (probably not covered in the 30 minute version)
- code samples: https://github.com/anthonywritescode/explains

## outline

### intro (~3 minutes)

- who am I?

### the meat of the presentation (the rest of the time budget)

(scheduling here is tentative, I'll probably cut or reorganize to better match
the flow / time budget)

- what does it mean to be "lazy" (~2 minutes)
- what is the new syntax (~1 minute)
- how does this work (`LOAD_GLOBAL`, etc.) (~2 minutes)

- use 1: "deferring slow modules to speed up some use cases"
    - a practical example using a real project
        - demonstrating a problem (`--help` is slow or `--version` is slow) (~1 minute)
        - using `importtime-waterfall` to find slow things (~5 minutes)

- use 2: "only used for a type annotation" (~2 minutes)
    - python3.14+ type annotations are already deferred (PEP 749)
    - previously sometimes in `if TYPE_CHECKING:` blocks
    - now you can `lazy import` them!

- use 3: "some *some* import cycles" (~4 minutes)
    - practical example
    - crash with a cycle (neat error message that I added!)
    - fixing it with `lazy` (and why it works)

- pitfall 1: no imports are checked (use a linter) (~1 minute)
- pitfall 2: it's pretty easy to accidentally un-lazy an import (~2 minutes)
    - practical example with `pre-commit` and `pyyaml`
    - *hopefully* by presentation time I'll have supporting linters via
      `flake8` to catch this and will be able to demo those as well

- protip: either profile or enable all (~2 minutes)
    - either enable them all (`-X lazy_imports=all`
    - or profile first to target particular modules

___

extended talk: additional time showcasing `future-lazy-imports` and how
I hacked this syntax into older pythons
