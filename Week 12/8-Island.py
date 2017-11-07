""" PSIT Week 12
Wiput Pootong (60070090)
Island
"""

def floodfill(i, j, row, col, island):
    """Return 1 if (i, j) and its neighors are part of the island, 0 otherwise."""
    count = 0
    if island[i][j] == 1:
        island[i][j] = 2
        eightdirections = [(1, 0), (-1, 0), (0, 1), (0, -1),
                           (1, 1), (1, -1), (-1, 1), (-1, -1)]
        newpositions = [(i+x, j+y) for x, y in eightdirections]
        for posx, posy in newpositions:
            if posx in range(0, row) and posy in range(0, col):
                floodfill(posx, posy, row, col, island)
        count = 1
    return count

def count_island(row, col, island):
    """Return total number of islands in the map."""
    count = 0
    for i in range(row):
        for j in range(col):
            count = count + floodfill(i, j, row, col, island)
    return count

def make_matrix():
    """Return number of rows, number of columns and matrix of island map."""
    row, col = [int(x) for x in input().split()]
    island = [[int(x) for x in input().split()] for _ in range(row)]
    return row, col, island

def main():
    """Get input for map and print number of islands."""
    row, col, island = make_matrix()
    print(count_island(row, col, island))

main()
