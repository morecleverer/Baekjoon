paper = [[0 for i in range(100)] for j in range(100)]
res = 0
n = int(input())

for i in range(n):

    a,b = map(int, input().split())

    for j in range(a,a+10):
        for k in range(b,b+10):
            if paper[j][k] == 0:
                paper[j][k] = 1
                res += 1

print(res)

