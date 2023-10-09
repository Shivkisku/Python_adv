class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

def add_linked_lists(l1, l2):
    dummy_head = ListNode()
    current = dummy_head
    carry = 0

    while l1 or l2 or carry:
        # Get the values from the linked lists or use 0 if they are None
        val1 = l1.value if l1 else 0
        val2 = l2.value if l2 else 0

        # Calculate the sum and carry
        total = val1 + val2 + carry
        carry = total // 10
        digit = total % 10

        # Create a new node with the digit and add it to the result linked list
        current.next = ListNode(digit)
        current = current.next

        # Move to the next nodes if they exist
        if l1:
            l1 = l1.next
        if l2:
            l2 = l2.next

    return dummy_head.next

# Helper function to create a linked list from a list of digits in reverse order
def create_linked_list(digits):
    dummy_head = ListNode()
    current = dummy_head

    for digit in digits:
        current.next = ListNode(digit)
        current = current.next

    return dummy_head.next

# Helper function to convert a linked list to a list of digits in reverse order
def linked_list_to_list(head):
    result = []
    current = head

    while current:
        result.append(current.value)
        current = current.next

    return result

# Example usage:
l1 = create_linked_list([9, 9])
l2 = create_linked_list([5, 2])
result = add_linked_lists(l1, l2)
print(linked_list_to_list(result))  # Output: [4, 2, 1] (99 + 25)
