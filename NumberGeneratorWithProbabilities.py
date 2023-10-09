import random

def generate_number_with_probability(numbers, probabilities):
    if len(numbers) != len(probabilities) or abs(sum(probabilities) - 1.0) > 1e-9:
        raise ValueError("Invalid input: Length of numbers and probabilities must be the same, and probabilities must sum to 1.")

    rand_num = random.uniform(0, 1)
    cumulative_probability = 0

    for num, prob in zip(numbers, probabilities):
        cumulative_probability += prob
        if rand_num < cumulative_probability:
            return num

# Example usage:
numbers = [1, 2, 3, 4]
probabilities = [0.1, 0.5, 0.2, 0.2]

result = generate_number_with_probability(numbers, probabilities)
print(result)
