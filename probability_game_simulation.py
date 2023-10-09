import random

def game1():
    rolls = 0
    while True:
        roll1 = random.randint(1, 6)
        rolls += 1
        if roll1 == 5:
            roll2 = random.randint(1, 6)
            rolls += 1
            if roll2 == 6:
                return rolls

def game2():
    rolls = 0
    while True:
        roll1 = random.randint(1, 6)
        rolls += 1
        if roll1 == 5:
            roll2 = random.randint(1, 6)
            rolls += 1
            if roll2 == 5:
                return rolls

# Simulate both games for a large number of trials
num_trials = 100000
total_cost_game1 = 0
total_cost_game2 = 0

for _ in range(num_trials):
    cost_game1 = game1()
    total_cost_game1 += cost_game1

    cost_game2 = game2()
    total_cost_game2 += cost_game2

# Calculate the expected values
expected_value_game1 = total_cost_game1 / num_trials
expected_value_game2 = total_cost_game2 / num_trials

print(f"Expected value of Game 1: ${expected_value_game1}")
print(f"Expected value of Game 2: ${expected_value_game2}")

if expected_value_game1 < expected_value_game2:
    print("Alice should choose Game 1.")
elif expected_value_game1 > expected_value_game2:
    print("Alice should choose Game 2.")
else:
    print("It doesn't matter which game Alice chooses.")
