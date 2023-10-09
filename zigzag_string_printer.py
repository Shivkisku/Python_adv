def print_zigzag(string, k):
    if k == 1:
        print(string)
        return

    lines = [''] * k
    current_line = 0
    direction = 1  # 1 for down, -1 for up

    for char in string:
        lines[current_line] += char
        if current_line == 0:
            direction = 1
        elif current_line == k - 1:
            direction = -1
        current_line += direction

    for line in lines:
        print(line)

# Example usage:
sentence = "thisisazigzag"
k = 4
print_zigzag(sentence, k)
