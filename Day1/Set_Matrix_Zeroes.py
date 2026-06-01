# Problem Statement - 
# Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.
# LeetCode Problem No. 73
# https://leetcode.com/problems/set-matrix-zeroes/description/


# BRUTE FORCE - TC: O(m×n) | SC: O(m+n)

class BruteForce:
    def setZeroes(self, matrix):
        n, m = len(matrix), len(matrix[0])

        rows, cols = [], []

        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 0:
                    rows.append(i)
                    cols.append(j)

        for r in rows:
            for j in range(m):
                matrix[r][j] = 0

        for c in cols:
            for i in range(n):
                matrix[i][c] = 0


# BETTER - TC: O(m×n) | SC: O(m+n)

class Better:
    def setZeroes(self, matrix):
        n, m = len(matrix), len(matrix[0])

        rows, cols = set(), set()

        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 0:
                    rows.add(i)
                    cols.add(j)

        for i in range(n):
            for j in range(m):
                if i in rows or j in cols:
                    matrix[i][j] = 0


# OPTIMAL - TC: O(m×n) | SC: O(1)

class Optimal:
    def setZeroes(self, matrix):
        n, m = len(matrix), len(matrix[0])

        fr = False
        fc = False

        for j in range(m):
            if matrix[0][j] == 0:
                fr = True

        for i in range(n):
            if matrix[i][0] == 0:
                fc = True

        for i in range(1, n):
            for j in range(1, m):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0

        for i in range(1, n):
            for j in range(1, m):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        if fr:
            for j in range(m):
                matrix[0][j] = 0

        if fc:
            for i in range(n):
                matrix[i][0] = 0
