import math

t = int(input())

for i in range(t):

    n,k = map(int,input().split())

    s = k*n + (n*n - n)/2

    ss = s//2

    g = math.floor(math.sqrt(k*k + 2*ss + 1))

    print(g)
    print((g-k+1)*(k+g)/2)


