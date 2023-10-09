def egyptian_fraction(a, b):
    fractions = []
    
    while a > 0:
        unit_fraction_denominator = (b + a - 1) // a  # Compute the next unit fraction's denominator
        fractions.append(f"1/{unit_fraction_denominator}")  # Add the unit fraction to the list
        a = a * unit_fraction_denominator - b  # Update the numerator
        
        # Ensure that a and b are coprime (their greatest common divisor is 1)
        gcd = math.gcd(a, b)
        a //= gcd
        b //= gcd
    
    return fractions

# Example usage:
import math
a = 4
b = 13
result = egyptian_fraction(a, b)
print(result)  
