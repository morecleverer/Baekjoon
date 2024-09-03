n = int(input())

res = 0
for i in range(n):

    isOk = True
    st = input()

    di = dict()

    di[st[0]] = 1

    for j in range(1, len(st)):
        if st[j - 1] == st[j]:
            continue
        else:
            di[st[j - 1]] = 0

            try:
                if di[st[j]] == 0:
                    isOk = False
                    break

            except:
                di[st[j]] = 1
    if isOk:
        res += 1
print(res)
