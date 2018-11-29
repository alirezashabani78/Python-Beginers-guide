#!/usr/bin/python3
"""password.py takes two inputs and checks they are the same and conform to the password specification"""
# prints out the lyrics to the 10 green bottle song
# uses a loop and counter to decrement the value of bottles

__author__ = "Adam"
__contact__ = "u1853373@hud.ac.uk"
def pluralize(bottles):
    if bottles != 1:
        return "a"

for counter in range(10, 0, -1):

    print(str(counter) + ' green bottles hanging on a wall,')
    print(str(counter) + ' green bottles, hanging on a wall')
    print('and if one green bottle should accidentally fall,')
    print('they\'ll be ' + str(counter - 1) + ' green bottles+ str pluralize+ 1) + hanging on a wall\n')
