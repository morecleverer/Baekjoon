def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


m, n = map(int, input().split())

m,n = m//gcd(m,n), n//gcd(m,n)

p, q = map(int, input().split())

p,q = p//gcd(max(p,q), min(p,q)), q//gcd(max(p,q),min(p,q))

gc = gcd(max(n, q), min(n, q))

fir = n // gc
sec = q // gc

res_s, res_m = m * sec + p * fir, n * sec

res_s, res_m = res_s//gcd(max(res_s,res_m),min(res_s, res_m)), res_m//gcd(max(res_s,res_m),min(res_s, res_m))

print(res_s, res_m)