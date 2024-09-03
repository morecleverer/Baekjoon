from collections import deque
import sys

input = sys.stdin.readline

n = input()

isqs = list(map(int, input().split()))

o = list(map(int, input().split()))

realqs = deque([])

for i in range(int(n)):

    if isqs[i] == 1:
        continue
    else:
        realqs.append(o[i])

n = int(input())

s = list(map(int, input().split()))


res = []
for i in s:
    realqs.appendleft(i)
    res.append(realqs.pop())

for i in res:
    print(i,end = " ")