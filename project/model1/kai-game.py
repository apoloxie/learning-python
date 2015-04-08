#!/usr/bin/env python
# vim:set nospell:

from random import randint

PROMPT="I'm thinking of a number from [0-100].  What is your guess? "

if __name__ == '__main__':
    print '-- Welcome to the Guessing Game! --'

    target = randint(0,100)
    guess = None

    while guess != target:
        guess = int(raw_input(PROMPT))

        if guess > target:
            print 'Your guess is too high :-('
        if guess < target:
            print 'Your guess is too low :-('

    print 'WOW!  You got it! :-)'
