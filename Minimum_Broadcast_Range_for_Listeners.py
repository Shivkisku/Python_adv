def min_broadcast_range(listeners, towers):
    listeners.sort()
    towers.sort()
    min_range = 0
    
    for listener in listeners:
        left_tower = None
        right_tower = None
        
        # Find the closest tower to the left
        for tower in towers:
            if tower <= listener:
                left_tower = tower
            else:
                break
        
        # Find the closest tower to the right
        for tower in reversed(towers):
            if tower >= listener:
                right_tower = tower
            else:
                break
        
        if left_tower is None:
            min_range = max(min_range, right_tower - listener)
        elif right_tower is None:
            min_range = max(min_range, listener - left_tower)
        else:
            min_range = max(min_range, min(listener - left_tower, right_tower - listener))
    
    return min_range

# Example usage:
listeners = [1, 5, 11, 20]
towers = [4, 8, 15]
result = min_broadcast_range(listeners, towers)
print(result)  # Output: 5
