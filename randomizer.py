#!/usr/bin/python3

#Author: Chris Martis

import random
import string

def randomizer(ftype=string.digits, size=10,qty=1):
    inptype = ftype
    #print(type(ftype))
    for i in range(qty):
        return(''.join(random.choice(inptype) for i in range(size)))


#Drive code
if __name__ == "__main__":

    randomizer()
'''
    ascii_upper = string.ascii_uppercase
    randomizer(ascii_upper, 10, 10)

    ascii_lower = string.ascii_lowercase
    randomizer(ascii_lower, 10, 10)

    letters = string.ascii_letters
    randomizer(letters, 10, 10)

    digits = string.digits
    randomizer(digits, 10, 10)

    punctuation = string.punctuation
    randomizer(punctuation, 10, 10)
 ''' 
