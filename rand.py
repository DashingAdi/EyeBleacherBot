from random import randint as ri


rn = ri(1,6)

with open('bleach.txt') as b:

    a = b.readlines()

    msg = "\n^I ^am ^a ^bot "

    rb = a[rn] + msg
