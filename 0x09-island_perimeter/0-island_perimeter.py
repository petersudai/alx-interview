#!/usr/bin/python3
"""
island_perimeter
"""


def island_perimeter(grid):
    """
    returns the perimeter of the island
    """
    perimeter = 0

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 1:
                # check top
                if i == 0 or grid[i-1][j] == 0:
                    perimeter += 1
                # check bottom
                if i == len(grid) - 1 or grid[i+1][j] == 0:
                    perimeter += 1
                # check left
                if j == 0 or grid[i][j-1] == 0:
                    perimeter += 1
                # check right
                if j == len(grid[i]) - 1 or grid[i][j+1] == 0:
                    perimeter += 1

    return perimeter
