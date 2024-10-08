import sys
#input = sys.stdin.readline()

from collections import deque

n = int(sys.stdin.readline())

q = deque()

for _ in range(n):
    a = sys.stdin.readline().split()

    if a[0] == "push":
        q.append(int(a[1]))

    elif a[0] == "pop":
        if len(q) == 0:
            print(-1)
        else:
            print(q[0])
            q.popleft()

    elif a[0] == "size":
        print(len(q))

    elif a[0] == "empty":
        if len(q) == 0:
            print(1)
        else:
            print(0)

    elif a[0] == "front":
        if len(q) == 0:
            print(-1)
        else:
            print(q[0])


    elif a[0] == "back":
        if len(q) == 0:
            print(-1)
        else:
            print(q[len(q) - 1])


