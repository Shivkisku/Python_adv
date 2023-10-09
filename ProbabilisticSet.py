import random

class ProbabilisticSet:
    def __init__(self):
        self.values = []
        self.value_set = {}

    def add(self, value):
        if value not in self.value_set:
            self.values.append(value)
            self.value_set[value] = len(self.values) - 1

    def check(self, value):
        return value in self.value_set

# Example usage:
probabilistic_set = ProbabilisticSet()

# Add values to the set
for value in range(10):
    probabilistic_set.add(value)

# Check if values are in the set
for value in range(15):
    is_in_set = probabilistic_set.check(value)
    print(f"{value} is in set: {is_in_set}")
