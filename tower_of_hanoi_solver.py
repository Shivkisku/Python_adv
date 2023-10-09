def tower_of_hanoi(n, source_rod, auxiliary_rod, target_rod):
    if n == 1:
        print(f"Move 1 from {source_rod} to {target_rod}")
        return
    tower_of_hanoi(n - 1, source_rod, target_rod, auxiliary_rod)
    print(f"Move {n} from {source_rod} to {target_rod}")
    tower_of_hanoi(n - 1, auxiliary_rod, source_rod, target_rod)

# Example usage:
n = 3
tower_of_hanoi(n, 1, 2, 3)
