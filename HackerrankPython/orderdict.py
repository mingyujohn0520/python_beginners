from time import time
from random import randint
from collections import OrderedDict


dict1 = OrderedDict()
players = list("ABCDEFGH")
start = time()

for i in range(0, 8):
    input()
    end = time()
    p = players.pop(randint(0, 7 - i))
    #print(i + 1, p, end - start)
    dict1[p] = (i + 1, end - start)
    print(p, dict1[p])
    