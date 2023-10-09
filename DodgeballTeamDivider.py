def divide_teams(students):
    def dfs(student, team):
        if student in visited:
            return team == teams[student]

        visited.add(student)
        teams[student] = team

        for enemy in students[student]:
            if not dfs(enemy, 1 - team):
                return False

        return True

    visited = set()
    teams = {}

    for student in students:
        if student not in visited and not dfs(student, 0):
            return False

    team_0 = {student for student, team in teams.items() if team == 0}
    team_1 = {student for student, team in teams.items() if team == 1}

    return team_0, team_1

# Example 1
students1 = {
    0: [3],
    1: [2],
    2: [1, 4],
    3: [0, 4, 5],
    4: [2, 3],
    5: [3]
}

result1 = divide_teams(students1)
print(result1)  # Output: ({0, 1, 4, 5}, {2, 3})

# Example 2
students2 = {
    0: [3],
    1: [2],
    2: [1, 3, 4],
    3: [0, 2, 4, 5],
    4: [2, 3],
    5: [3]
}

result2 = divide_teams(students2)
print(result2)  # Output: False
