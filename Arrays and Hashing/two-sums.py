from typing import List


def twoSum(nums: List[int], target: int) -> List[int]:
    # Solution 1
    # indexes = []
    # for i in range(0, len(nums)):
    #     for k in range(0, len(nums)):
    #         if nums[i] + nums[k] == target:
    #             if (
    #                 not indexes.__contains__(i)
    #                 and not indexes.__contains__(k)
    #                 and i != k
    #             ):
    #                 indexes.append(i)
    #                 indexes.append(k)

    # return indexes

    # Solution 2
    # n = len(nums)
    # indexes = set()
    # for i in range(0, n):
    #     for j in range(0, n):
    #         if nums[i] + nums[j] == target:
    #             if i != j:
    #                 indexes.add(i)
    #                 indexes.add(j)

    # return list(indexes)

    # Solution 3
    n = len(nums)
    indexes = set()
    for i in range(0, n):
        v = target - nums[i]

        if v in nums:
            index = nums.index(v)
            if nums.index(v) != i:
                indexes.add(i)
                indexes.add(index)

    return list(indexes)


print("Test 1: [2, 7, 11, 15], 9:", twoSum([2, 7, 11, 15], 9))
# [0,1]
print("Test 2: [3,2,4], 6:", twoSum([3, 2, 4], 6))
# [1,2]
