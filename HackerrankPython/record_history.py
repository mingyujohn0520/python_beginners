from random import randint
from collections import deque

N = randint(0, 100)
history = deque([], 5)

def guess(k):
    if k == N:
        print("your answer is correct")
        return True
    elif k < N:
        print("{} is less than N".format(k))
    else:
        print("{} is greater than N".format(k))
        return False

while True:
    line = input("please input a number: ")
    if line.isdigit():
        k = int(line)
        history.append(k)
        if guess(k):
            break
    elif line == "history" or line == "h?":
        print(list(history))