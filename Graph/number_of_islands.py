def dfs(grid, i, j):
    if i < 0 or i >= len(grid) or \
        j < 0 or j >= len(grid[0]) or\
            grid[i][j] != '1':
        return

    grid[i][j] = '0'

    dfs(grid, i+1, j)
    dfs(grid, i-1, j)
    dfs(grid, i, j+1)
    dfs(grid, i, j-1)


def number_of_islands(grid):

    if not grid:
        return 0

    count = 0

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == '1':
                dfs(grid, i, j)
                count += 1
    return count


if __name__ == "__main__":

    grid1 = [['1', '1', '1', '1', '0'],
             ['1', '1', '0', '1', '0'],
             ['1', '1', '0', '0', '0'],
             ['0', '0', '0', '0', '0']]

    print("number of islands from grid1:", number_of_islands(grid1))

    grid2 = [['1', '1', '0', '0', '0'],
             ['1', '1', '0', '0', '0'],
             ['0', '0', '1', '0', '0'],
             ['0', '0', '0', '1', '1']]

    print("number of islands from grid2:", number_of_islands(grid2))
