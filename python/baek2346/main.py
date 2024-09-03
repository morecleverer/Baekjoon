from collections import deque

n = int(input())

dq = deque()

l = list(map(int, input().split()))

res = []

for i in range(1,len(l)+1):

    dq.append([i,l[i-1]])

while not len(dq) == 0:
    a = dq.popleft()

    res.append(a[0])

    if len(dq) == 0:
        break

    if a[1] > 0:
        for i in range(a[1]-1):
            dq.append(dq.popleft())
    else:
        for i in range(abs(a[1])):
            dq.appendleft(dq.pop())


for i in res:
    print(i, end=" ")
