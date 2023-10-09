def count_friend_groups(friendship):
    def dfs(node, group):
        visited.add(node)
        group.add(node)
        for neighbor in friendship[node]:
            if neighbor not in visited:
                dfs(neighbor, group)

    visited = set()
    friend_groups = []

    for student in friendship:
        if student not in visited:
            group = set()
            dfs(student, group)
            friend_groups.append(group)

    return len(friend_groups)

# Example friendship list
friendship = {
    0: [1, 2],
    1: [0, 5],
    2: [0],
    3: [6],
    4: [],
    5: [1],
    6: [3]
}

result = count_friend_groups(friendship)
print(result)  # Output: 3 (Three friend groups)
