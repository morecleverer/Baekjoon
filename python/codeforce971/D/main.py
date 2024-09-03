t = int(input())

for _ in range(t):

    n = int(input())

    same_x, tri = 0,0

    p_set = set()

    for i in range(n):

        p = tuple(map(int,input().split()))

        p_set.add(p)

        if (p[0], 0 if p[1] == 1 else 1) in p_set:
            same_x += 1

        if (p[0]-1, 0 if p[1] == 1 else 1) in p_set and (p[0]+1, 0 if p[1] == 1 else 1) in p_set:
            tri += 1

        if (p[0]-2, 0 if p[1] == 0 else 1) in p_set and (p[0]-1, 0 if p[1] == 1 else 1) in p_set:
            tri += 1

        if (p[0]+2, 0 if p[1] == 0 else 1) in p_set and (p[0]+1, 0 if p[1] == 1 else 1) in p_set:
            tri += 1

    print(same_x*(len(p_set)-2)+tri)







