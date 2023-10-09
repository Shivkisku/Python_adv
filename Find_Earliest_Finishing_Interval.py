class ListNode:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.random = None

def deep_clone_linked_list(head):
    if not head:
        return None

    # Step 1: Create new nodes and insert them into the original list
    current = head
    while current:
        new_node = ListNode(current.value)
        new_node.next = current.next
        current.next = new_node
        current = new_node.next

    # Step 2: Set random pointers for the new nodes
    current = head
    while current:
        if current.random:
            current.next.random = current.random.next
        current = current.next.next

    # Step 3: Separate the original list from the new list
    cloned_head = head.next
    current = head
    while current:
        new_node = current.next
        current.next = new_node.next
        current = current.next
        if current:
            new_node.next = current.next
        else:
            new_node.next = None

    return cloned_head

# Example usage:
# Create a sample linked list with random pointers
node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node1.next = node2
node2.next = node3
node1.random = node3
node2.random = node1
node3.random = node2

cloned_head = deep_clone_linked_list(node1)

# Verify the cloned list
while cloned_head:
    print(f"Value: {cloned_head.value}, Random: {cloned_head.random.value if cloned_head.random else 'None'}")
    cloned_head = cloned_head.next
