class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def bfs(grid: List[List[str]], r: int, c: int, seen: set[tuple[int, int]]):
            if (r, c) in seen or grid[r][c] == '0': return
            seen.add((r, c))
            moves = [(0, -1), (0, 1), (-1, 0), (1, 0)]
            for ri, ci in moves:
                row = r + ri
                col = c + ci
                if row >= 0 and row < len(grid) and col >= 0 and col < len(grid[0]):
                    bfs(grid, row, col, seen)
        seen = set()
        res = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == '1' and (row, col) not in seen:
                    res += 1
                    bfs(grid, row, col, seen)
        return res

        