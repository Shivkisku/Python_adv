def findStrobogrammatic(N):
    def helper(n, N):
        if n == 0:
            return [""]
        if n == 1:
            return ["0", "1", "8"]

        inner = helper(n - 2, N)
        result = []

        for num in inner:
            if n != N:
                result.append("0" + num + "0")
            result.append("1" + num + "1")
            result.append("8" + num + "8")
            result.append("6" + num + "9")
            result.append("9" + num + "6")

        return result

    if N <= 0:
        return []
    elif N == 1:
        return ["0", "1", "8"]
    else:
        return [num for num in helper(N, N) if num[0] != "0"]

# Test the findStrobogrammatic function
N = 5
result = findStrobogrammatic(N)
print(result)
