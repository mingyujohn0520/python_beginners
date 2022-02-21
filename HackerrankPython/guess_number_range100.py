from random import randint

N = randint(0, 100)

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
        if guess(k):
            break
# what I can think about the solution
# while True:
#     k = int(input("please input a number: "))
#     if guess(k):
#         break