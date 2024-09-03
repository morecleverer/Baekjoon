
t = int(input())

for _ in range(t):

    n = int(input())

    stk = list()

    for __ in range(n):

        row = input()

        for i, ch in enumerate(row):
            if ch == '#':
                stk.append(i+1)
                break

    for __ in range(len(stk)):
        print(stk.pop(), end = ' ')


