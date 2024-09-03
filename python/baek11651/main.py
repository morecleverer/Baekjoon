from collections import deque
n = int(input())

li = []

for i in range(n):
    l = list(map(int, input().split()))

    li.append(l[::-1])

li.sort()
