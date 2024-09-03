from collections import deque
import sys

input = sys.stdin.readline

n = int(input())

li = deque(list(map(int, input().split())))
wait = []

cur = 1

isOk = True

while len(li)>0:
    if li[0] == cur:
        li.popleft()
        cur += 1
    elif len(wait) > 0 and wait[-1] == cur:
        wait.pop()
        cur += 1

    elif len(wait) == 0 or li[0] < wait[-1]:
        wait.append(li.popleft())
    else:
        isOk = False
        break

if isOk:
    print("Nice")
else:
    print("Sad")