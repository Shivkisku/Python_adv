import random

def toss_biased():
    # Replace this with your actual biased coin toss function.
    # For demonstration purposes, I'm using random.choice([0, 1]) with a fixed probability.
    return random.choice([0, 1, 1])  # Example: 1 has a higher probability

def toss_unbiased():
    while True:
        result1 = toss_biased()
        result2 = toss_biased()

        if result1 != result2:
            return result1

# Example usage:
unbiased_result = toss_unbiased()
print(unbiased_result)  # Output: Either 0 or 1 with a 50-50 chance
