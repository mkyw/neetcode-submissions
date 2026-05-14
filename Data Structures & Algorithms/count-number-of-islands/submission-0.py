class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        island_count = 0
        def dfs(i, j):
            if i > 0:
                if grid[i-1][j] == "1":
                    grid[i-1][j] = 0
                    dfs(i-1, j)
            if i < len(grid)-1:
                if grid[i+1][j] == "1":
                    grid[i+1][j] = 0
                    dfs(i+1, j)
            if j > 0:
                if grid[i][j-1] == "1":
                    grid[i][j-1] = 0
                    dfs(i, j-1)
            if j < len(grid[i])-1:
                if grid[i][j+1] == "1":
                    grid[i][j+1] = 0
                    dfs(i, j+1)

        for i in range(0, len(grid)):
            for j in range(0, len(grid[i])):
                # print((i, j), grid[i][j])
                if grid[i][j] == "1":
                    island_count += 1
                    dfs(i, j)
        
        return island_count
