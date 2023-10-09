def lowestCostToFillSeats(seats):
    m = sum(seats)  # Count of people
    n = len(seats)  # Total number of seats
    target = m  # Target position for the first person

    cost = 0  # Initialize cost to 0
    for i in range(n):
        if seats[i] == 1:
            cost += abs(i - target)  # Calculate the cost for the current person
            target += 1  # Move the target for the next person

    return cost

# Example usage:
if __name__ == "__main__":
    seats = [0, 1, 1, 0, 1, 0, 0, 0, 1]
    result = lowestCostToFillSeats(seats)
    print(result)  