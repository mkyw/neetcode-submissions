class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxArea = 0
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        def dfs(r, c):
            if (r < 0 or c < 0 or r >= len(grid) or
                c >= len(grid[r]) or grid[r][c] == 0
            ):
                return 0

            grid[r][c] = 0
            total = 1
            for dr, dc in directions:
                total += dfs(r + dr, c + dc)

            return total
        
        for r in range(0, len(grid)):
            for c in range(0, len(grid[r])):
                if grid[r][c] == 1:
                    currArea = dfs(r, c)
                    maxArea = max(maxArea, currArea)
        
        return maxArea