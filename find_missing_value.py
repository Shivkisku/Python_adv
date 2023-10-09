def find_missing_value(array):
    # sorting the array
    array.sort()

    # if the array is empty we return 1 since 1 is the first positive number.
    if len(array) == 0:
        return 1

    # otherwise we search.
    else:

        # take the first of the array.
        k = array[0]
        # if k is bigger than two then we should return 1 since the array is sorted.
        if k >= 2:
            return 1
        # otherwise we search for it
        for i in range(len(array)):
            # if k is not like the current element than this k is missing number.
            if k != array[i]:
                return k

            # if not the case we increment k.
            k += 1

            # if we increment and k is 0 we re-increment it.
            if k == 0:
                k += 1
        # finally return k if the number was out the range of the array.
        # like [1,2,3] here the missing is 4.
        return k


# testing the code
print(find_missing_value([3, 4, -1, 1]))
print(find_missing_value([1, 2, 0]))
print(find_missing_value([1, 2, 3, 4, 6]))
print(find_missing_value([]))