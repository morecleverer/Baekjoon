n, m = map(int, input().split())

dogam = dict()
donum = dict()

for i in range(n):
    a = input()

    dogam[a] = i + 1
    donum[i + 1] = a

res = []
for j in range(m):

    res.append(input())

for b in res:
    if b in dogam.keys():
        print(dogam[b])
    else:
        print(donum[int(b)])
