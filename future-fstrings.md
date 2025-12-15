# customizing python's syntax with terrible hacks

## abstract

What if macros, new syntax, and more were just a `pip install` away?

In this talk I'll show how a load-bearing comment and an obscure python
import system feature make this a reality!

We'll dive into each of these features and how they can be chained together
to enable custom source pre-processing.

I'll demo how I used these techniques to make f-strings work in python 2,
added support for dictionary unpacking in python, and more!

## supplemental information

30 minute talk ideally

notes / outline: https://github.com/anthonywritescode/cfp/blob/main/future-fstrings.md

- project: https://github.com/asottile/future-fstrings
- project: https://github.com/asottile/dict-unpacking-at-home

previous presentations:

- python now has dict unpacking? https://youtu.be/eqiM0xRmFJg
- what is a `.pth` file? https://youtu.be/mzxQrgvuRFg
- code samples: https://github.com/anthonywritescode/explains

## outline

### intro (~5 minutes)

- who am I?
- y tho? (it started out as a joke how did it end up like this?)

### the meat of the presentation (~25 minutes)

- python 2 f-strings demo (~2 minutes)
- basic explanation of encodings (utf-8 to turn bytes into text) (3 minutes)
- registering custom encodings in python (1 minute)
- ok registering custom encodings requires code -- how to automate it?
- `.pth` files: special import system magic (5 minutes)
- packaging a `.pth` file (3 minutes)
- putting that together: a custom encoding which performs source manipulation! (10 minutes)
    - parse / unparse token stream (`tokenize-rt`)
