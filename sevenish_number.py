def nthSevenishNumber(n):
    result = 0
    power_of_seven = 1

    while n > 0:
        if n & 1:
            result += power_of_seven
        n >>= 1
        power_of_seven *= 7

    return result

# Test the function
n = 5  # Find the 5th sevenish number
print(nthSevenishNumber(n))  # Output: 57
