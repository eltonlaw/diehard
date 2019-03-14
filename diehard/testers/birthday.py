# -*- coding: utf-8 -*-
""" birthday.py """
from diehard.utils import preprocess
from diehard.utils import chunker

import numpy as np
from scipy.stats import poisson
from scipy.special import gammaincc
from collections import defaultdict

# NOTE: Do not change these parameters! This test only works with these:
intsize = 32
nbits = 24
nms = 2**9

@preprocess
def birthday(samples):
	'''
	The idea is to choose m birthdays in a year of n days. Then calculate the 
	spacings between birthdays. Most of these intervals will be unique, but 
	some may occur more than once. Count how many intevals occurred more than 
	once.

	Example
	-------
	Say you randomly select m=4 birthdays in a year of n=365 days. Imagine the
	selected birthdays are June 15, October 28, March 3, and April 24. The 
	intervals are 52: (March 3 - April 24, April 24 - June 15) and 
	135: (June 15 - October 28). Only 1 of these intervals occurred more than
	once (52), so our test statistic would be 1.

	Parameters
	----------
	samples: array of arrays
		Each inner array must contain 512 32-bit ints. len(samples) is the
		sample size. (This test takes ~3s for a sample size of 100.)

	Returns
	-------
	p-value: float
		Likelihood of outcome if generator of samples were truly random.
		p-values > 0.01: test passes.
	'''
	assert all([len(arr) == nms for arr in samples]), \
			"`samples` should be a list of arrays containing 512 32-bit ints"
	assert all([0 <= val < 2**intsize and isinstance(val, np.int64) for arr in samples for val in arr]), \
			"`samples` should be a list of arrays containing 512 32-bit ints"

	nsamples = len(samples)
	tstats = defaultdict(int)
	
	sampleTs(samples, tstats, nsamples)

	return chisq_poisson(tstats, pow(nms,3) / pow(2,nbits+2), intsize * nsamples)

def sampleTs(samples, tstats, nsamples):
	mask = 2**nbits - 1

	for arr in samples:
		for i in range(intsize):
			# shift bits and take lowest 24 bits
			birthdays = sorted([rotl(val, i, intsize) & mask for val in arr])
			intervals = defaultdict(int)
			
			for j in range(1, len(birthdays)):
				intervals[birthdays[j] - birthdays[j-1]] += 1

			t = len([val for val in intervals.values() if val > 1])
			tstats[t] += 1
	return tstats

def chisq_poisson(observed, mu, nsamples):
	dim = max(observed.keys()) + 1
	x = np.arange(dim)
	expected = nsamples * poisson.pmf(x, mu)

	chisq = 0
	for i in range(dim):
		chisq += (observed[i] - expected[i])**2 / expected[i]

	return gammaincc((dim - 1) / 2, chisq / 2)

def rotl(x, i, intsize):
	return (((x << i) | (x >> (intsize - i))) & (2**intsize - 1))