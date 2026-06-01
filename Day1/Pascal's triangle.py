# Problem Statement -
# Given an integer numRows, return the first numRows of Pascal's triangle.
# In Pascal's triangle, each number is the sum of the two numbers directly above it.
#
# LeetCode Problem No. 118
# https://leetcode.com/problems/pascals-triangle/


# BRUTE FORCE - TC: O(n³) | SC: O(1)

class BruteForce:
    def generate(self, numRows):
        result = []

        for row in range(numRows):
            current_row = []

            for col in range(row + 1):
                value = 1

                for i in range(col):
                    value = value * (row - i)
                    value = value // (i + 1)

                current_row.append(value)

            result.append(current_row)

        return result


# BETTER - TC: O(n²) | SC: O(1) 

class Better:
    def generate(self, numRows):
        result = []

        for row in range(numRows):
            current_row = [1] * (row + 1)

            for col in range(1, row):
                current_row[col] = result[row - 1][col - 1] + result[row - 1][col]

            result.append(current_row)

        return result


# OPTIMAL - TC: O(n²) | SC: O(1)

class Optimal:
    def generate(self, numRows):
        result = []

        for row in range(numRows):
            current_row = []
            value = 1

            for col in range(row + 1):
                current_row.append(value)
                value = value * (row - col) // (col + 1)

            result.append(current_row)

        return result
