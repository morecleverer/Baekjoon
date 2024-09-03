import heapq
import sys

input = sys.stdin.readline

#help(heapq)


hq = []

n = int(input())

for i in range(n):

    a = int(input())

    if a == 0:
        if len(hq) == 0:
            print(0)
        else:
            print(heapq.heappop(hq))
    else:
        heapq.heappush(hq, a)