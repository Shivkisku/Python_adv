def push_dominoes(dominoes):
    n = len(dominoes)
    forces = [0] * n  # Initialize forces array

    # Calculate forces from left to right
    force = 0
    for i in range(n):
        if dominoes[i] == 'R':
            force = n
        elif dominoes[i] == 'L':
            force = 0
        else:
            force = max(0, force - 1)
        forces[i] += force

    # Calculate forces from right to left
    force = 0
    for i in range(n - 1, -1, -1):
        if dominoes[i] == 'L':
            force = n
        elif dominoes[i] == 'R':
            force = 0
        else:
            force = max(0, force - 1)
        forces[i] -= force

    # Determine the orientation of each domino based on forces
    result = []
    for force in forces:
        if force > 0:
            result.append('R')
        elif force < 0:
            result.append('L')
        else:
            result.append('.')

    return ''.join(result)

# Example usage:
dominoes1 = ".L.R....L"
dominoes2 = "..R...L.L"

result1 = push_dominoes(dominoes1)
result2 = push_dominoes(dominoes2)

print(result1)  # Output: "LL.RRRLLL"
print(result2)  # Output: "..RR.LLLL"
