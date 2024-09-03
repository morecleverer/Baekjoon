t = int(input())

for i in range(t):
    x,y,k = map(int,input().split())

    x_way = x//k if x%k==0 else x//k +1
    y_way = y//k if y%k==0 else y//k +1

    if x_way > y_way:
        print(2*x_way-1)

    elif y_way > x_way:
        print(2*y_way)

    else:
        print(2*x_way)
