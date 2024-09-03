n = int(input())

a = list(map(int,input().split()))

num_dict = dict()

for i in a:
    try:
        num_dict[i] += 1
    except:
        num_dict[i] = 1

nn = int(input())

b = list(map(int, input().split()))

res = []

for i in b:
    try:
        res.append(num_dict[i])
    except:
        res.append(0)

for i in res:
    print(i, end=" ")