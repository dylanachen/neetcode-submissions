class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        positions = len(matrix) * len(matrix[0])
        n = len(matrix[0])

        l = 0
        r = positions - 1

        while l <= r:
            mid = l + ((r - l) // 2)

            i = mid // n
            if matrix[i][mid - (i * n)] == target:
                return True
            elif matrix[i][mid - (i * n)] < target:
                l = mid + 1
            else:
                r = mid - 1
        
        return False