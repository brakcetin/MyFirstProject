#!/usr/bin/python

def displayPathtoPrincess(n, grid):
    princess_position = []
    bot_position = []
    for i in range(n):
        for j in range(n):
            if grid[i][j] == 'm':
                bot_position = (i, j)

            if grid[i][j] == 'p':
                princess_position = (i, j)

    x_diff = princess_position[0] - bot_position[0]
    y_diff = princess_position[1] - bot_position[1]

    if x_diff > 0:
        for _ in range(x_diff):
            print("DOWN")
    if x_diff < 0:
        for _ in range(-x_diff):
            print("UP")
    if y_diff > 0:
        for _ in range(y_diff):
            print("RIGHT")
    if y_diff < 0:
        for _ in range(-y_diff):
            print("LEFT")


# Take user input for grid size
N = int(input("Enter the size of the grid (odd integer, 3 <= N < 100): "))

# Take user input for the grid
grid = []
print("Enter the grid:")
for _ in range(N):
    row = input().strip()
    grid.append(row)

# Output the moves to rescue the princess
displayPathtoPrincess(N, grid)