class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()

        def helper_dfs(row, col):
            # Base Cases
            # Out of bounds
            if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0]):
                return
            # It is water
            if grid[row][col] == "0":
                return

            # Already visited
            if (row, col) in visited:
                return
            
            visited.add((row, col))

            helper_dfs(row - 1, col)
            helper_dfs(row + 1, col)
            helper_dfs(row, col - 1)
            helper_dfs(row, col + 1)

        island_cnt = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == "1" and (row, col) not in visited:
                    island_cnt += 1
                    helper_dfs(row, col)
        return island_cnt