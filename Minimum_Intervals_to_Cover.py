def find_small(array):
    mina = array[0][0]
    index = 0
    for ind in range(len(array)):
        if array[ind][0] < mina:
            index = ind
    return index


def big_all(value, array):
    result = True
    for i in array:
        if i > value:
            result = False
    return result


intervals = [(30, 75), (0, 50), (60, 150)]

mins = []
for i in intervals:
    if len(mins) == 0:
        var = find_small(intervals)
        mins.append(intervals[var][1])
        del intervals[var]
    else:
        var = find_small(intervals)
        if not big_all(intervals[var][0], mins):
            mins.append(intervals[var][0])
        del intervals[var]

print(len(mins))