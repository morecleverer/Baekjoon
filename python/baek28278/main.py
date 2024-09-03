import sys
n = int(sys.stdin.readline())

stk = []

for i in range(n):

    k = input().split()

    order = int(k[0])

    if order == 1:
        stk.append(int(k[1]))

    elif order == 2:
        if len(stk) == 0:
            print(-1)
        else:
            print(stk.pop())

    elif order == 3:
        print(len(stk))

    elif order == 4:
        if len(stk) == 0:
            print(1)
        else:
            print(0)

    elif order == 5:

        if not len(stk) == 0:
            print(stk[-1])
        else:
            print(-1)