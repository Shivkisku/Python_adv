from collections import deque

class OrderLog:
    def __init__(self, N):
        self.log = deque(maxlen=N)

    def record(self, order_id):
        self.log.append(order_id)

    def get_last(self, i):
        if i < 1 or i > len(self.log):
            return None
        return self.log[-i]

# Example usage:
N = 5  # Set the maximum number of order ids to keep in the log
order_log = OrderLog(N)

order_log.record("order1")
order_log.record("order2")
order_log.record("order3")

print(order_log.get_last(1))  # Output: "order3"
print(order_log.get_last(2))  # Output: "order2"
