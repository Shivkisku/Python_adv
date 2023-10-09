class StockTracker:
    def __init__(self):
        self.data = []  # List to store (timestamp, price) pairs

    def add(self, timestamp, price):
        self.data.append((timestamp, price))

    def update(self, timestamp, price):
        # Update an existing data point if the timestamp matches
        for i, (ts, _) in enumerate(self.data):
            if ts == timestamp:
                self.data[i] = (timestamp, price)
                break

    def remove(self, timestamp):
        # Remove a data point with a specific timestamp if it exists
        self.data = [(ts, price) for ts, price in self.data if ts != timestamp]

    def max(self):
        if not self.data:
            return None
        return max(price for _, price in self.data)

    def min(self):
        if not self.data:
            return None
        return min(price for _, price in self.data)

    def average(self):
        if not self.data:
            return None
        total_price = sum(price for _, price in self.data)
        return total_price / len(self.data)

# Example usage:
tracker = StockTracker()
tracker.add(1633932600, 100)  # (timestamp, price)
tracker.add(1633932700, 110)
tracker.add(1633932800, 120)
print("Max:", tracker.max())  # Max: 120
print("Min:", tracker.min())  # Min: 100
print("Average:", tracker.average())  # Average: 110.0
tracker.update(1633932700, 115)
print("Updated Max:", tracker.max())  # Updated Max: 120
tracker.remove(1633932600)
print("Removed Min:", tracker.min())  # Removed Min: 115
