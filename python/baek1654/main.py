#실패

def isOkay(lis, num, count):

    s = 0
    next_s = 0

    for i in lis:
        s += i//num
        next_s += i//(num+1)

    if s == count and (not next_s == count):
        return 0

    elif s < count:
        return -1

    elif s == count and next_s == count:

        return 1

    else:
        return 1


k,n = map(int,input().split())


leng = []

for _ in range(k):
    leng.append(int(input()))


a = sum(leng)//n


left = 0
right = a
tries = 0
mid = a//2

while True:

    if left >= right:
        print(mid)
        break

    mid = (left+right)//2

    num = isOkay(leng,mid, n)
    tries += 1

    if tries >= a:
        print(mid)
        break

    if num == 0:
        print(mid)
        break

    elif num == 1:
        left = mid+1

    elif num == -1:
        right = mid



