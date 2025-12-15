# explaining weird stuff via python's compilation pipeline

## abstract

Did you know python is compiled?

This talk will show how source code gets processed and eventually compiled
into bytecode.  The viewer will learn the basics of what a "stack machine" is
and how that bytecode gets interpreted.

Along the way we'll show some quirks in python's syntax and execution and
explain them using the tokenization, ast parsing, and bytecode stack
machine disassembly.

## supplemental information

30 minute talk ideally, can be 45 (can expand more examples).

notes / outline: https://github.com/anthonywritescode/cfp/blob/main/explaining-weird-things.md

previous presentations (parts of these are combined into this talk):
- university of michigan guest lecture: https://youtu.be/G2yPbg2fgQY
- python is compiled? https://youtu.be/FPJdre3mbD4
- weird python identity quirk https://youtu.be/w4GasVbjIbA
- how does swap work in python? https://youtu.be/cMiqfkpMh08
- python has an optimizer? https://youtu.be/i8uNgEchr20
- tuples vs lists performance https://youtu.be/8nvfOjvOF5w
- python implicit string joining https://youtu.be/5Zto6VYsNsI
- python implicitly returns None? https://youtu.be/-zH0qqDtd4w
- code samples: https://github.com/anthonywritescode/explains

## outline

### intro (~5 minutes)

- who am I?
- why have I spent so much time learning these things?

### the meat of the presentation (the rest of the time budget)

- python is compiled? (quick demo of `.pyc` files)
- first step: tokenization
    - show tokenization of file
    - `tokenize_rt` and additional "unimportant" tokens
    - weird: half-triple-quoted-strings
- second step: abstract syntax tree
    - grammar of python transforms token stream into syntax tree
    - PEG grammar of python
    - weird: `False == False in [False]`
    - weird: `a == not b`
- third step: some magic turns that into bytecode
    - demo of stack machine on simple `add` example
    - peephole optimizer
    - implicit return `None`
    - swap
    - weird: `x = ([],); x[0] += [1]`
    - weird: `'s' * 2 is 's' * 2` vs `* i`
