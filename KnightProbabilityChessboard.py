def knightProbability(N, K, r, c):
    # Possible knight moves
    moves = [(2, 1), (1, 2), (-1, 2), (-2, 1),
             (-2, -1), (-1, -2), (1, -2), (2, -1)]
    
    # Initialize a 3D DP array to store probabilities
    dp = [[[0] * N for _ in range(N)] for _ in range(K+1)]
    
    # Initial position probability is 1
    dp[0][r][c] = 1
    
    # Calculate the probabilities for each move
    for step in range(1, K+1):
        for x in range(N):
            for y in range(N):
                for dx, dy in moves:
                    newX, newY = x + dx, y + dy
                    if 0 <= newX < N and 0 <= newY < N:
                        dp[step][newX][newY] += dp[step-1][x][y] / 8.0
    
    # Sum all probabilities after K moves
    probability = sum(dp[K][i][j] for i in range(N) for j in range(N))
    
    return probability

# Example usage:
N = 8
K = 3
r = 0
c = 0
result = knightProbability(N, K, r, c)
print(f"Probability that the knight remains on the board after {K} moves: {result}")
