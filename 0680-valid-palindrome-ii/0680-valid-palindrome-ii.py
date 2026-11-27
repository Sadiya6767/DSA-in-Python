class Solution:

    def validPalindrome(self, s):

        def checkPalindrome(left, right):

            while left < right:

                if s[left] != s[right]:
                    return False

                left += 1
                right -= 1

            return True

        left = 0
        right = len(s) - 1

        while left < right:

            if s[left] != s[right]:

                return (
                    checkPalindrome(left + 1, right)
                    or
                    checkPalindrome(left, right - 1)
                )

            left += 1
            right -= 1

        return True