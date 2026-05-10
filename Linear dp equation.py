

def extended_gcd(a, b):
    if a == 0:
        return b, 0, 1
    gcd, x1, y1 = extended_gcd(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    return gcd, x, y

def solve_lde(a, b, c):
    # Step 1: Find GCD using Extended Euclidean
    gcd, x0, y0 = extended_gcd(a, b)
    
    # Step 2: Check if solution exists
    if c % gcd != 0:
        return None  # No integer solution possible
    
    # Step 3: Scale the results
    # If ax + by = gcd, then a(x*c/gcd) + b(y*c/gcd) = c
    factor = c // gcd
    x = x0 * factor
    y = y0 * factor
    
    return gcd, x, y

# User Input
print("\n--- Linear Diophantine Equation Solver (ax + by = c) ---")
try:
    val_a = int(input("Enter a: "))
    val_b = int(input("Enter b: "))
    val_c = int(input("Enter c: "))

    result = solve_lde(val_a, val_b, val_c)

    if result:
        gcd, x, y = result
        print(f"\nSolution exists because GCD({val_a}, {val_b}) = {gcd}, which divides {val_c}.")
        print(f"One particular solution: x = {x}, y = {y}")
        print(f"Verification: ({val_a} * {x}) + ({val_b} * {y}) = {val_c}")
    else:
        print(f"\nNo integer solution exists because GCD of {val_a} and {val_b} does not divide {val_c}.")
except ValueError:
    print("Please enter valid integers.")