# five-dice-pwd
**gen-five-dice.py**
This script generates a multi-word passphrase.
- It simulates rolling 5 dice by generating a random 5-digit number.
- It searches the accompanying EFF Large Wordlist to find the word that corresponds to that number.

The optional integer argument sets the length of the output phrase in words.
It defaults to 5 words if no arguments are given.
```shell
$ ./gen-five-dice.py 4
Simulated dice rolls: 15634-52346-31614-42346
Password string: citation-rocket-gag-obsession
```
