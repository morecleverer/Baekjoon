from collections import deque
import sys

input = sys.stdin.readline

n = int(input())

for i in range(n):

    li = list(input())
    li = li[:-1]

    left = deque()
    right = deque()

    for j in li:


        if j == "<":
            if len(left) == 0:
                continue
            else:
                right.appendleft(left.pop())

        elif j == ">":
            if len(right) == 0:
                continue
            else:
                left.append(right.popleft())

        elif j == "-":
            if len(left) == 0:
                continue
            else:
                left.pop()

        else:
            left.append(j)


    while(len(right)>0):
        left.append(right.popleft())

    for i in left:
        print(i,end = "")
    print()