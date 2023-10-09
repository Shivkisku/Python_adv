class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def partition_linked_list(head, k):
    # Initialize two lists for nodes less than k and nodes greater than or equal to k
    less_than_k_head = less_than_k_tail = Node(None)
    greater_than_or_equal_to_k_head = greater_than_or_equal_to_k_tail = Node(None)

    current = head

    while current:
        if current.data < k:
            less_than_k_tail.next = current
            less_than_k_tail = current
        else:
            greater_than_or_equal_to_k_tail.next = current
            greater_than_or_equal_to_k_tail = current

        current = current.next

    # Connect the two lists and set the end of the second list to None
    less_than_k_tail.next = greater_than_or_equal_to_k_head.next
    greater_than_or_equal_to_k_tail.next = None

    # Return the head of the merged list
    return less_than_k_head.next

# Helper function to print the linked list
def print_linked_list(head):
    current = head
    while current:
        print(current.data, end=" -> ")
        current = current.next
    print("None")

# Example usage:
# Create the linked list: 5 -> 1 -> 8 -> 0 -> 3
head = Node(5)
head.next = Node(1)
head.next.next = Node(8)
head.next.next.next = Node(0)
head.next.next.next.next = Node(3)

k = 3
partitioned_head = partition_linked_list(head, k)
print_linked_list(partitioned_head)
