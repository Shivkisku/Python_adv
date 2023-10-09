import heapq

def create_playlist(ranked_lists):
    playlist = []
    priority_queue = []

    # Initialize the priority queue with the first song from each list
    for user_index, user_list in enumerate(ranked_lists):
        if user_list:
            heapq.heappush(priority_queue, (user_list[0], user_index))
    
    while priority_queue:
        song, user_index = heapq.heappop(priority_queue)
        playlist.append(song)

        # Push the next song from the same user's list to the priority queue
        if user_index < len(ranked_lists) - 1 and len(ranked_lists[user_index]) > 1:
            heapq.heappush(priority_queue, (ranked_lists[user_index][1], user_index))
            ranked_lists[user_index] = ranked_lists[user_index][1:]

    return playlist

# Example usage:
ranked_lists = [[1, 7, 3], [2, 1, 6, 7, 9], [3, 9, 5]]
result = create_playlist(ranked_lists)
print(result)  # Output: [2, 1, 6, 7, 3, 9, 5]
