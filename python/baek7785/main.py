n = int(input())


names = dict()

for i in range(n):

    name, h = input().split()

    if h == "enter":
        names[name] = 1
    elif h == "leave":
        names.pop(name)


for i in sorted(names.keys(), reverse= True):
    print(i)