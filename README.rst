.. image:: https://travis-ci.org/eltonlaw/diehard.svg?branch=master
    :target: https://travis-ci.org/eltonlaw/diehard
    
.. image:: https://img.shields.io/pypi/v/diehard.svg
    :target: https://pypi.python.org/pypi/diehard

Diehard
=======

Tests for randomness. Inspired by Robert G. Brown's random number Dieharder test suite and the Diehard tests

Read The Docs: https://diehard.readthedocs.io/en/latest/

Introduction
------------

From Wikipedia_, the "diehard tests are a battery of statistical tests for
measuring the quality of a random number generator. They were developed by
George Marsaglia over several years and first published in 1995 on a CD-ROM of
random numbers."

Following the Wikipedia link, the outputs of each test vary wildly and I couldn't figure
out a good way to aggregate them so I've for the most part left them as is.

This project was originally motivated from something I heard in an audiobook
(maybe Naked Statistics?), my memory is hazy but it went something a long the
lines of this. A blogger/statistician had calculated the statistical
probabilities of some public data numbers and come to the conclusion that they
weren't statisically likely to be organic, someone had fudged them. After a
fuss was kicked up and an investigation was started, it was proven that they
were right - one of the people in charge of the data recording/publishing or
something or other had thrown in some random numbers.

Not only is this rather vindicating, statistics got to kick some
ass in an easily understood and public way but it gave me a renewed sense of hope
for the ability of an individual to create change in the world. This package was
conceived with idea that it would provide the tools needed to something like
the above on a wider scale, autonomously.

Or at least that's the end goal.

.. _Wikipedia: https://en.wikipedia.org/wiki/Diehard_tests



