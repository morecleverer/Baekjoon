from collections import deque
import sys

input = sys.stdin.readline

n = int(input())

q = deque()

for i in range(n):

    a = list(input().split())

    if a[0] == "1":
        q.appendleft(int(a[1]))

    elif a[0] == "2":
        q.append(int(a[1]))

    elif a[0] == "3":
        if len(q) == 0:
            print(-1)
        else:
            print(q.popleft())

    elif a[0] == "4":
        if len(q) == 0:
            print(-1)
        else:
            print(q.pop())

    elif a[0] == "5":
        print(len(q))

    elif a[0] == "6":
        if len(q) == 0:
            print(1)
        else:
            print(0)

    elif a[0] == "7":
        if len(q) == 0:
            print(-1)
        else:
            print(q[0])

    elif a[0] == "8":
        if len(q) == 0:
            print(-1)
        else:
            print(q[-1])