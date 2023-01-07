#!/usr/bin/python3

from os import system

system('clear')
x = int(input('input an integer'))
for y in range(x):
    print(' '*y+'#')
for y in range(x):
    print(' '*(x-y)+'#')
for y in range(x//2):
    print(' '*(x//2-y)+'#'+' '*(y*2)+'#')
for y in range(x*2+1):
    print(' '*(abs(y-x))+'#'+f'absolute val of ({y}-{x}) is {abs(y-x)}')
for y in range(x*2+1):
    print(' '*(x-(abs(y-x)))+'#'+f'{x} minus absolute val of ({y}-{x}) is {x-abs(y-x)}')
for y in range(x*2+1):
    print(' '*(abs(y-x))+'#'+' '*(x-(abs(y-x)))*2+'#')
for y in range(x*2+1):
    print(' '*(abs(y-x))+'#'*(((x-(abs(y-x)))*2)-1))
