

def extended_gcd(a, b):
    if a == 0:
        return b, 0, 1
    
    gcd, x1, y1 = extended_gcd(b % a, a)
    
    # Update x and y using results of recursive call
    x = y1 - (b // a) * x1
    y = x1
    
    return gcd, x, y

# User Input
print("--- Extended Euclidean Algorithm (ax + by = gcd(a,b)) ---")
try:
    a = int(input("Enter value for a: "))
    b = int(input("Enter value for b: "))

    gcd, x, y = extended_gcd(a, b)

    print(f"\nResults:")
    print(f"GCD: {gcd}")
    print(f"Coefficients: x = {x}, y = {y}")
    print(f"Equation: ({a} * {x}) + ({b} * {y}) = {gcd}")
except ValueError:
    print("Please enter valid integers.")