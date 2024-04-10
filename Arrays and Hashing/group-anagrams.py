# Group Anagrams
# https://leetcode.com/problems/group-anagrams

from collections import defaultdict


class Solution:
    # brute force solution
    # def groupAnagrams(strs):
    #     map = {}
    #     for s in strs:
    #         sorted_str = "".join(sorted(s))
    #         if sorted_str in map:
    #             map[sorted_str].append(s)
    #         else:
    #             map[sorted_str] = [s]
    #     return list(map.values())

    def groupAnagrams(strs):
        # Create a defaultdict with default value of an empty list
        anagram_groups = defaultdict(list)

        # Iterate over each string in the input list
        for word in strs:
            # Sort the characters in the word to create a key
            key = "".join(sorted(word))
            # Append the word to the list of anagrams for the key
            anagram_groups[key].append(word)

        # Return the values of the defaultdict as a list of lists
        return list(anagram_groups.values())


solution = Solution


print("Test 1:", solution.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
