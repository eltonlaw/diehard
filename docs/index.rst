.. diehard documentation master file, created by
   sphinx-quickstart on Sat Feb 24 15:43:54 2018.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

diehard
=====================================


Quick Reference
---------------

.. toctree::
   API <api/index>
   Contributing Notes <contributing_notes>

Introduction
------------

From Wikipedia_, the "diehard tests are a battery of statistical tests for measuring the quality of a random number generator. They were developed by George Marsaglia over several years and first published in 1995 on a CD-ROM of random numbers."

Following that link, the outputs of each test vary wildly and I couldn't figure out a good way to aggregate them so I've for the most part left them as is (or that was the intent, there is the competing interest of making it easy to parse).

This project was originally motivated from something I heard in an audiobook (maybe Naked Statistics?), my memory is hazy but it went something a long the lines of this. A blogger had calculated the statistical probabilities of some public data numbers and come to the conclusion that they weren't likely to be real, someone had fudged them. After a fuss was kicked up and an investigation was started, it was proven that they were right - one of the people in charge of the data recording or publishing or something had thrown in some random numbers. Not only is this rather awesome because statistics got to kick some ass

but it gave me a renewed sense of hope for the possibility of an individual to constitute change in what seems occasionally like a broken world.

Or at least that's the end goal, right now it's just yet another unfinished open source Python project (or YAUOSPP for short). This project welcomes contributions.

.. _Wikipedia: https://en.wikipedia.org/wiki/Diehard_tests
