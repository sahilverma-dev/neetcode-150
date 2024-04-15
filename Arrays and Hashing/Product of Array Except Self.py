# https://leetcode.com/problems/product-of-array-except-self/


"""
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.
"""


class Solution:
    def productExceptSelf(self, nums):
        # brute force 1
        """
        make a new array
        Iterate throw the threw the nums array and append product of all nums element except the current indexed element

        the problem with this solution is, it is not optimized and in O(n^2) we need O(n)
        doesn't work on [0,0]
        """
        # answer_list = []
        # for i in nums:
        #     product = 1
        #     for j in range(len(nums)):
        #         if i != nums[j]:
        #             product *= nums[j]
        #     answer_list.append(product)
        # return answer_list
        """
        to make the solution in O^
        """
        n = len(nums)
        left_products = [1] * n
        right_products = [1] * n
        new_array = [1] * n

        for i in range(1, n):
            left_products[i] = left_products[i - 1] * nums[i - 1]

        for i in range(n - 2, -1, -1):
            right_products[i] = right_products[i + 1] * nums[i + 1]

        for i in range(n):
            new_array[i] = left_products[i] * right_products[i]

        return new_array


s = Solution()

# Example 1
print(s.productExceptSelf([1, 2, 3, 4]))  # [24,12,8,6]

# Example 2
print(s.productExceptSelf([-1, 1, 0, -3, 3]))  # [0,0,9,0,0]

# Example 3
print(s.productExceptSelf([0, 0]))  # [0,0]
