from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m, n = len(matrix), len(matrix[0])
        cols, rows = set(), set()

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    cols.add(j)
                    rows.add(i)

        for j in cols:
            for i in range(m):
                matrix[i][j] = 0

        for i in rows:
            for j in range(n):
                matrix[i][j] = 0

