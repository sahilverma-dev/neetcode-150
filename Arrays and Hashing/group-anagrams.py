# Group Anagrams
# https://leetcode.com/problems/group-anagrams


class Solution:
    # brute force solution
    def groupAnagrams(strs):
        map = {}
        for s in strs:
            sorted_str = "".join(sorted(s))
            if sorted_str in map:
                map[sorted_str].append(s)
            else:
                map[sorted_str] = [s]
        return list(map.values())


solution = Solution

print("Test 1:", solution.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
