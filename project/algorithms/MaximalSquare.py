from typing import List

class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        cnt = 1
        m = min(len(matrix), len(matrix[0]))

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == "1":
                    con = False
                    while cnt < m:
                        for i in range(len(matrix) - cnt):
                            for j in range(len(matrix[0]) - cnt):
                                if not (matrix[i][j] == "1" and matrix[i+1][j] == "1" and matrix[i][j+1] == "1" and matrix[i+1][j+1] == "1"):
                                    matrix[i][j] = "0"
                                else:
                                    con = True

                        if not con:
                            break
                        con = False
                        cnt+=1

                    return cnt**2
        return 0