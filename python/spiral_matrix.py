class Solution(object):
    def spiralOrder(self, matrix):
        
        if not matrix:
            return []
        
        result = []
        n = len(matrix)
        m = len(matrix[0])
        
        # 4 directions of the matrix
        top = 0
        left = 0
        right = m - 1
        bottom = n - 1

        while len(result) < n * m:
            for col in range(left, right + 1):
                if len(result) < n * m:
                    result.append(matrix[top][col])
            for row in range(top + 1, bottom):
                if len(result) < n * m:
                    result.append(matrix[row][right])
            for col in range(right, left - 1, -1):
                if len(result) < n * m:
                    result.append(matrix[bottom][col])
            for row in range(bottom - 1, top, -1):
                if len(result) < n * m:
                    result.append(matrix[row][left])
            
            top += 1
            left += 1
            right -= 1
            bottom -= 1










        