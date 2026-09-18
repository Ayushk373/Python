def grid_paths(rows, cols):

    dp = [[0] * cols for _ in range(rows)]

    # First row
    for j in range(cols):
        dp[0][j] = 1

    # First column
    for i in range(rows):
        dp[i][0] = 1

    # Fill remaining cells
    for i in range(1, rows):
        for j in range(1, cols):
            dp[i][j] = dp[i-1][j] + dp[i][j-1]

    return dp[rows-1][cols-1]


print(grid_paths(3, 3))
