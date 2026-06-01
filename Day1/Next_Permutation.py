# Problem Statement -
# Given an array of integers nums, find the next permutation of nums.
# https://leetcode.com/problems/next-permutation/description/
# LeetCode Problem No. 31
# https://leetcode.com/problems/next-permutation/

# BRUTE FORCE - TC: O(n! × n) | SC: O(n! × n)

from itertools import permutations

class BruteForce:
    def nextPermutation(self, nums):
        perms = sorted(set(permutations(nums)))

        current = tuple(nums)

        for i in range(len(perms)):
            if perms[i] == current:
                if i == len(perms) - 1:
                    nums[:] = list(perms[0])
                else:
                    nums[:] = list(perms[i + 1])
                return


# BETTER - TC: O(n log n) | SC: O(1)

class Better:
    def nextPermutation(self, nums):
        n = len(nums)

        pivot = -1

        for i in range(n - 2, -1, -1):
            if nums[i] < nums[i + 1]:
                pivot = i
                break

        if pivot == -1:
            nums.reverse()
            return

        for i in range(n - 1, pivot, -1):
            if nums[i] > nums[pivot]:
                nums[i], nums[pivot] = nums[pivot], nums[i]
                break

        nums[pivot + 1:] = sorted(nums[pivot + 1:])


# OPTIMAL - TC: O(n) | SC: O(1)

class Optimal:
    def nextPermutation(self, nums):
        n = len(nums)

        index = -1

        for i in range(n - 2, -1, -1):
            if nums[i] < nums[i + 1]:
                index = i
                break

        if index == -1:
            nums.reverse()
            return

        for i in range(n - 1, index, -1):
            if nums[i] > nums[index]:
                nums[i], nums[index] = nums[index], nums[i]
                break

        left = index + 1
        right = n - 1

        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
