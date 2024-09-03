def hanoi(num, start, end):
    if num == 1:
        print(f"{start} {end}")

    else:
        hanoi(num-1,start,6-end-start)
        print(f"{start} {end}")
        hanoi(num-1,6-end-start,end)

n = int(input())

count = 1
for _ in range(n-1):
    count = 2*count + 1

print(count)


hanoi(n,1,3)