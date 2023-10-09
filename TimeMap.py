class TimeMap:
    def __init__(self):
        # Initialize a dictionary to store key-value pairs and their corresponding timestamps.
        self.data = {}

    def set(self, key, value, time):
        # Check if the key exists in the dictionary.
        if key in self.data:
            self.data[key].append((time, value))
        else:
            # If the key does not exist, create a list to store its values and timestamps.
            self.data[key] = [(time, value)]

    def get(self, key, time):
        if key in self.data:
            # Retrieve the list of values and timestamps for the given key.
            values = self.data[key]
            # Binary search to find the closest timestamp that is less than or equal to the given time.
            left, right = 0, len(values) - 1
            while left <= right:
                mid = left + (right - left) // 2
                timestamp, value = values[mid]
                if timestamp == time:
                    return value
                elif timestamp < time:
                    left = mid + 1
                else:
                    right = mid - 1
            # If no exact timestamp is found, return the value associated with the closest previous timestamp.
            if right >= 0:
                return values[right][1]
        return None

# Example usage:
d = TimeMap()
d.set(1, 1, 0)
d.set(1, 2, 2)
print(d.get(1, 1))  # Output: 1
print(d.get(1, 3))  # Output: 2
d.set(1, 1, 5)
print(d.get(1, 0))  # Output: None
print(d.get(1, 10))  # Output: 1
d.set(1, 1, 0)
d.set(1, 2, 0)
print(d.get(1, 0))  # Output: 2
