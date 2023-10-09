def find_celebrity(N):
    potential_celebrity = 0

    # First pass: Identify a potential celebrity
    for i in range(1, N):
        if knows(potential_celebrity, i):
            potential_celebrity = i

    # Second pass: Verify if the potential celebrity is a celebrity
    for i in range(N):
        if i != potential_celebrity and (knows(potential_celebrity, i) or not knows(i, potential_celebrity)):
            return -1  # No celebrity found

    return potential_celebrity

# Example usage:
# Replace knows(a, b) with your actual implementation
def knows(a, b):
    # Implementation of the knows function goes here
    pass

N = 4  # Number of people
celebrity = find_celebrity(N)
if celebrity != -1:
    print(f"The celebrity is person {celebrity}")
else:
    print("No celebrity found")
