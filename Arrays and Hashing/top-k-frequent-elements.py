# https://leetcode.com/problems/top-k-frequent-elements/description/

# Top K Frequent Elements
# Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.


class Solution:
    """
    brute force 1
    1. for every element in nums store the count value for iteration in a map
    2. return the k number of keys with higher values
    """

    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        count_map = {}
        for num in nums:
            if count_map.get(num) is not None:
                count_map[num] += 1
            else:
                count_map[num] = 1

        sorted_keys = sorted(count_map, key=count_map.get, reverse=True)
        return sorted_keys[:k]


s = Solution()

# Example 1
print(s.topKFrequent([1, 1, 1, 2, 2, 3], 2))

# Example 2
print(s.topKFrequent([4, 1, -1, 2, -1, 2, 3], 2))
