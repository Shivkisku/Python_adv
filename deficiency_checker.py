def get_factors(num):
    factors = []
    for i in range(1, num):
        if num % i == 0:
            factors.append(i)
    return factors

def is_deficient(num):
    factors = get_factors(num)
    sum_of_factors = sum(factors)
    return sum_of_factors < 2 * num

def find_deficient_numbers_in_range(start, end):
    deficient_numbers = []
    for num in range(start, end + 1):
        if is_deficient(num):
            deficient_numbers.append(num)
    return deficient_numbers

# Example usage:
num_to_check = 12
print(f"{num_to_check} is deficient: {is_deficient(num_to_check)}")

start_range = 1
end_range = 50
deficient_numbers_in_range = find_deficient_numbers_in_range(start_range, end_range)
print(f"Deficient numbers in the range {start_range} to {end_range}: {deficient_numbers_in_range}")
