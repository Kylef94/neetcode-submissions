class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        low = 0
        high = len(matrix[0]) - 1
        for row in range(len(matrix)):
            if target < matrix[row][low]:
                return False
            if target <= matrix[row][high]:
                while low <= high:
                    mid = low + (high - low) // 2
                    if matrix[row][mid] == target:
                        return True
                    elif matrix[row][mid] < target:
                        low = mid + 1
                    else:
                        high = mid - 1
        return False

        
        