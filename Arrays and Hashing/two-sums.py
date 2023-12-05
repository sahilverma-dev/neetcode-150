from typing import List


def twoSum(nums: List[int], target: int) -> List[int]:
    indexes = []
    for i in range(0, len(nums)):
        for k in range(0, len(nums)):
            if nums[i] + nums[k] == target:
                if (
                    not indexes.__contains__(i)
                    and not indexes.__contains__(k)
                    and i != k
                ):
                    indexes.append(i)
                    indexes.append(k)

    return indexes


result = twoSum([3, 2, 4], 6)

print(result)
