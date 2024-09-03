import sys

input = sys.stdin.readline

a = list(input())

bomb = list(input())
bomb = bomb[:-1]

st = []


for i in a[:-1]:

    st.append(i)

    if i == bomb[-1] and len(st) >= len(bomb):
        if st[-1*len(bomb):] == bomb:
            for j in range(len(bomb)):
                st.pop()

if len(st) == 0:
    print("FRULA")
else:
    for i in st:
        print(i,end="")