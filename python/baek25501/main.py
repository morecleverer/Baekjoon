
def isPal(txt, num):

    if len(txt) <= 1:
        return [1, num+1]

    if not txt[0] == txt[-1]:
        return [0,num+1]

    else:
        return isPal(txt[1:-1],num+1)


n = int(input())

for _ in range(n):
    text = input()

    a = isPal(text,0)

    for i in a:
        print(i, end=" ")
    print()