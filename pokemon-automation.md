# catching (shiny) pokémon with python!

## abstract

With over 1000 unique monsters (add counting) "catching them all" can be quite
the daunting task!  What if we could automate the process?

Let's use python to automate gameplay on real hardware!

In this talk you'll find:

- the basics of image processing in python (computer vision, optical character
  recognition, segmentation, etc.)
- how python interacts with the hardware to simulate button presses

No prior knowledge of pokémon, hardware, or computer vision is necessary to
enjoy this talk.

## supplemental information

30 minute talk ideally, can be 45.

notes / outline: https://github.com/anthonywritescode/cfp/blob/main/pokemon-automation.md

project: https://github.com/asottile/nintendo-microcontrollers

previous presentations: https://www.youtube.com/playlist?list=PLWBKAf81pmOYZoIyNPAnR7i56KV1JaRr0

## outline

### intro (~5 minutes)

- who am I?
- what is a shiny pokemon (aka: why automate this at all?)
- a mini stats lesson :)

### the project (the rest of the time budget)

- hardware setup (nintendo switch, simplest -- easiest to live demo)
- software setup (basics of capturing the screen)
- a few useful techniques (will narrow down / expand to fit time)
    - thresholding (detecing "is something X colorish")
    - OCR (reading text on the screen)
    - "who's that pokemon?" (matching known sprite silhouettes)
    - k means
- custom state management
    - originally 6-deep nested `while` => custom typesafe state machine

### further (~5 minutes)

- extending this to other more difficult hardware
    - soldering test points on gba / 3ds / wii / joycon
