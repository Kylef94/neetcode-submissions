class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        def dfs(heights: List[List[int]], r: int, c: int, 
                ocean: set[tuple[int, int]]):
            ocean.add((r, c))
            moves = [(0, -1), (0, 1), (-1, 0), (1, 0)]
            for ri, ci in moves:
                row = r + ri
                col = c + ci
                if 0 <= row < len(heights) and \
                0 <= col < len(heights[0]) and \
                (row, col) not in ocean and \
                heights[row][col] >= heights[r][c]:
                    dfs(heights, row, col, ocean)
            return

            
        pacific = set()
        atlantic = set()

        for c in range(len(heights[0])):
            dfs(heights, 0, c, pacific)
        
        for r in range(len(heights)):
            dfs(heights, r, 0, pacific)
        
        for c in range(len(heights[0])):
            dfs(heights, len(heights) - 1, c, atlantic)
        
        for r in range(len(heights)):
            dfs(heights, r, len(heights[0]) - 1, atlantic)


        return [[r , c] for r, c in pacific.intersection(atlantic)]
        