def letterCombinations(digits, mapping):
    def backtrack(combination, index):
        if index == len(digits):
            results.append(combination)
            return

        current_digit = digits[index]
        if current_digit in mapping:
            for letter in mapping[current_digit]:
                backtrack(combination + letter, index + 1)

    if not digits:
        return []

    results = []
    backtrack("", 0)
    return results

# Example usage:
if __name__ == "__main__":
    digit_mapping = {
        "2": ["a", "b", "c"],
        "3": ["d", "e", "f"],
        "4": ["g", "h", "i"],
        "5": ["j", "k", "l"],
        "6": ["m", "n", "o"],
        "7": ["p", "q", "r", "s"],
        "8": ["t", "u", "v"],
        "9": ["w", "x", "y", "z"]
    }

    input_digits = "23"
    combinations = letterCombinations(input_digits, digit_mapping)
    print(combinations)
