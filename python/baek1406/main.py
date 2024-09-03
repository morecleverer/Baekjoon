from collections import deque
import sys

input = sys.stdin.readline

k = list(input())

left = deque(k[:-1])
right = deque()

n = int(input())

for i in range(n):
    a = list(input().split())

    if a[0] == "L":
        if len(left) == 0:
            continue
        else:
            right.appendleft(left.pop())

    elif a[0] == "D":
        if len(right) == 0:
            continue
        else:
            left.append(right.popleft())

    elif a[0] == "B":
        if len(left) == 0:
            continue
        else:
            left.pop()

    elif a[0] == "P":
        left.append(a[1])


while(len(right)>0):
    left.append(right.popleft())

for i in left:
    print(i,end = "")
