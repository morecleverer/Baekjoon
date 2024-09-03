import sys

input = sys.stdin.readline

x = input()

a = set(map(int, input().split()))
b = set(map(int, input().split()))

c = a.difference(b)

c = list(c)

c.sort()

if len(c) == 0:
    print(0)
else:
    print(len(c))
    for i in c:
        print(i,end=" ")
