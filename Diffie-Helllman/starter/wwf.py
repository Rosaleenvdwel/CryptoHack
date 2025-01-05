def extended_gcd(a, b):
    """Return gcd of a and b, and coefficients x, y such that ax + by = gcd(a, b)"""
    if a == 0:
        return b, 0, 1
    gcd, x1, y1 = extended_gcd(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    return gcd, x, y

def mod_inverse(g, p):
    """Return the modular inverse of g modulo p"""
    gcd, x, _ = extended_gcd(g, p)
    if gcd != 1:
        raise ValueError(f"No modular inverse for {g} modulo {p}")
    else:
        return x % p  #makes result positive

# Given values
p = 991
g = 209

#calutes inverse
inverse = mod_inverse(g, p)
print(f"The inverse of {g} modulo {p} is: {inverse}")