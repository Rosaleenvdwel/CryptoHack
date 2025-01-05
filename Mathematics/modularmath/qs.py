p = 29
ints = [14, 6, 11]

def find_quadratic_residues(p, integers):
    residues = {}
    
    for x in integers:
        for a in range(p):
            if (a * a) % p == x:
                residues[x] = a  #first found root
                break  

    return residues

quadratic_residues = find_quadratic_residues(p, ints)

#print to show results 
for x, root in quadratic_residues.items():
    print(f"{x} is a quadratic residue with square root {root}")


if quadratic_residues:
    smallest_root = min(quadratic_residues.values())
    print(f"The smallest root among the quadratic residues is: {smallest_root}")
else:
    print("No quadratic residues found.")