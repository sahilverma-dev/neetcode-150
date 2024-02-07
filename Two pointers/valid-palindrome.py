class Solution:
    def isPalindrome(self, s: str) -> bool:
        # brute force solution

        # newStr = ""
        # for i in s:
        #     if i.isalnum():
        #         newStr += i.lower()

        # return newStr == newStr[::-1]

        # Two pointers solution
        newStr = ""
        for i in s:
            if i.isalnum():
                newStr += i.lower()

        l, r = 0, len(newStr) - 1

        while r >= l:
            if newStr[l] != newStr[r]:
                return False

            l, r = l + 1, r - 1

        return True


solution = Solution()


print("Test 1", solution.isPalindrome("A man, a plan, a canal: Panama"))
print("Test 1", solution.isPalindrome("A man, a plan, a canal: Panamasfasda"))
