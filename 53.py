class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix:
            return []
        ans = []
        m, n = len(matrix), len(matrix[0])
        top, bottom, left, right = 0, m - 1, 0, n - 1
        while top < bottom and left < right:
            for i in range(left, right):
                ans.append(matrix[top][i])
            for i in range(top, bottom):
                ans.append(matrix[i][right])
            for i in range(right, left, -1):
                ans.append(matrix[bottom][i])
            for i in range(bottom, top, -1):
                ans.append(matrix[i][left])
            top += 1
            bottom -= 1
            left += 1
            right -= 1
        if top == bottom and left == right:
            ans.append(matrix[top][left])
        elif top == bottom:
            for i in range(left, right + 1):
                ans.append(matrix[top][i])
        elif left == right:
            for i in range(top, bottom + 1):
                ans.append(matrix[i][left])
        return ans