class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxArea = 0
        visited = set()

        def dfs(r, c):
            if (r < 0 or c < 0 or r >= len(grid) or
                c >= len(grid[r]) or grid[r][c] == 0 or
                (r,c) in visited
            ):
                return 0

            visited.add((r,c))
            return (1 + dfs(r - 1, c) +
                        dfs(r + 1, c) +
                        dfs(r, c - 1) +
                        dfs(r, c + 1))
        
        for r in range(0, len(grid)):
            for c in range(0, len(grid[r])):
                maxArea = max(maxArea, dfs(r, c))
        
        return maxArea