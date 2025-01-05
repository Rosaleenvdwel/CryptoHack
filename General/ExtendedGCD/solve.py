def extended_gcd(p, q):
    if q == 0:
        return p, 1, 0
    else:
            gcd, u1, v1 =extended_gcd(q, p % q)
            u = v1
            v = u1 - (p // q) *v1 
            return gcd, u, v

p = 26513
q = 32321

gcd, u, v = extended_gcd(p, q)

print(f"gcd({p}, {q}) = {gcd}")
print(f"u = {u}, v = {v}")