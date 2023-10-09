import random

def rand5():
    return random.randint(1, 5)

def rand7():
    while True:
        # Generate a random number between 1 and 25 using rand5()
        # This is done by generating (rand5() - 1) * 5 + (rand5() - 1)
        num = (rand5() - 1) * 5 + (rand5() - 1)

        # If the generated number is in the range 1 to 21, return (num % 7) + 1
        if num < 21:
            return (num % 7) + 1

# Test the rand7() function
for _ in range(10):
    print(rand7())
