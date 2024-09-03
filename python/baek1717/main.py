import sys

input = sys.stdin.readline

n,m = map(int, input().split())

li = [i for i in range(n+1)]



def find(a):
    if li[a] == a:
        return a
    else:
        return find(li[a])



for i in range(m):

    x,a,b = map(int, input().split())

    if x == 0:
        if a==b:
            continue

        li[max(find(a),find(b))] = li[min(find(a),find(b))]

    else:
        if find(a) == find(b):
            print("YES")
        else:
            print("NO")

    #print(li)
