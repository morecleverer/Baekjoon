n = int(input())

a = set()

a.update(set(map(int,input().split())))

m = int(input())


j = list(map(int,input().split()))
for k in j:
    if k in a:
        print(1, end=" ")
    else:
        print(0, end=" ")


