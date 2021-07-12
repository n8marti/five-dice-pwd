#!/usr/bin/python3

'''
Simulate a roll of 5 dice and get the matching series of password words
from the EFF large wordlist.
https://www.eff.org/deeplinks/2016/07/new-wordlists-random-passphrases
'''

import os
import random
import sys
from pathlib import Path

about = f"""Usage: {sys.argv[0]} [integer]

This script generates a multi-word passphrase.
- It simulates rolling 5 dice by generating a random 5-digit number.
- It searches the accompanying EFF Large Wordlist to find the word that corresponds to that number.

The optional integer argument sets the length of the output phrase in words.
It defaults to 5 words if no arguments are given.

$ {sys.argv[0]} 4
Simulated dice rolls: 15634-52346-31614-42346
Password string: citation-rocket-gag-obsession
"""

length = 5
if len(sys.argv) > 1:
    if sys.argv[1] in ['help', '--help', '-h']:
        print(about)
        exit()
    else:
        length = int(sys.argv[1])

def get_digit():
    """
    Return a single digit from 1 to 6.
    """
    digit = str(random.randint(1, 6))
    return digit

def get_dice_roll():
    """
    Return string of 5 digits from 1 to 5.
    """
    combo = [str(get_digit()) for i in range(5)]
    return ''.join(combo)

def get_roll_series(quantity):
    """
    Return list of 5 dice rolls of 5 dice each.
    """
    rolls = [get_dice_roll() for i in range(quantity)]
    return rolls

def get_word_from_roll(word_dict, roll):
    """
    Return word that corresponds to dice roll.
    """
    if roll in word_dict.keys():
        return word_dict[roll]

parent_dir = Path(sys.argv[0]).resolve().parent
infile = parent_dir / 'passwords_eff_large_wordlist.txt'

with open(infile, 'r') as f:
    lines = f.readlines()

word_dict = {}
for line in lines:
    word_dict[line.split()[0]] = line.split()[1]

rolls = [roll for roll in get_roll_series(length)]
words = [get_word_from_roll(word_dict, roll) for roll in rolls]
print(f"Simulated dice rolls: {'-'.join(rolls)}")
print(f"Password string: {'-'.join(words)}")
