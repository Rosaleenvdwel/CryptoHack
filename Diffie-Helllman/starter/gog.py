def gcd(a, b):
    """Compute the greatest common divisor of a and b."""
    while b:
        a, b = b, a % b
    return a

def is_primitive(g, p):
    """Check if g is a primitive element of Fp."""
    order = p - 1
    for q in range(2, order + 1):
        if order % q == 0:  #check if q is a factor of order
            if pow(g, order // q, p) == 1:  # Check for primitive
                return False
    return True

def find_smallest_primitive(p):
    """Find the smallest primitive element in Fp."""
    for g in range(2, p):  #start from 2
        if is_primitive(g, p):
            return g
    return None


p = 28151

#find the smallest primitive element
smallest_primitive = find_smallest_primitive(p)
print(f"The smallest primitive element in F_{p} is: {smallest_primitive}")