#!/usr/bin/env python
# Copyright (c) 2017 kang@insecure.ws
# Licensed under the terms of the GPLv2

import math
import sys
import gzip
import time
from tqdm import *

# Ported entropy() and entropy_ideal() from Revelation (https://revelation.olasagasti.info/)
# Copyright (c) 2003-2006 Erik Grinaker
# Licensed under the terms of the GPLv2
def entropy(string):
    p = [ float(string.count(c)) / len(string) for c in dict.fromkeys(list(string)) ]
    entropy = - sum([ ap * math.log(ap) / math.log(2.0) for ap in p ])
    return entropy

def entropy_ideal(length):
    """Ideal Shannon entropy"""
    p = 1.0 / length
    ideal = (-1.0 * length * p * math.log(p) / math.log(2.0))
    return ideal

def entropy_acceptable(length, percent=80):
    """Within 'percent' of ideal target is acceptable."""
    ideal = entropy_ideal(length)
    acceptable = (percent*ideal)/100
    return acceptable

def pw_check(pw_str):
    print("Checking your password is within acceptable range of the ideal entropy (80% close to ideal target entropy)")
    acceptable_p = entropy_acceptable(len(pw_str))
    pw_p = entropy(pw_str)

    if pw_p < acceptable_p:
        print("Your password is not safe, please choose a safer password. Your entropy {}, target entropy {}.".format(pw_p, acceptable_p))
        return False
    print("You password has {} entropy for a length of {} - ideal entropy is {} and you're close enough ( above {}).".format(pw_p, len(pw_str), entropy_ideal(len(pw_str)), acceptable_p))
    return True

def check_known(pw_str):
    with gzip.open('pw_list.txt.gz', 'rb') as fd:
        for line in tqdm(fd, desc='Searching for commonly used passwords...'):
            l = line.decode('utf-8', 'ignore').strip('\n').strip('\r')
            if l == pw_str:
                print("You password is a commonly used password, that's not safe.")
                return False

    return True

def main(pw_str):
    if not pw_check(pw_str):
        return False
    if not check_known(pw_str):
        return False
    print("Success! This password look potentially like a good one for it's length.")
    return True

if __name__ == "__main__":
    if not main(sys.argv[1]):
        sys.exit(1)
