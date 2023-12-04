from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(set(nums)) < len(nums)

# Example usage
solution = Solution()
result = solution.containsDuplicate([1, 1, 2, 3, 4])
print(result)
