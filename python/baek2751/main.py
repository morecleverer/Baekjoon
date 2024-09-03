import sys
input = sys.stdin.readline


a = []

n = int(input())

for _ in range(n):
    a.append(int(input()))


a.sort()

for i in a:
    print(i)


