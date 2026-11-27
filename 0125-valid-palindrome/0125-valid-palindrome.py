class Solution(object):
    def isPalindrome(self, s):

        s = s.lower()

        left = 0
        right = len(s)- 1

        while left < right:
            # skip alphanumeric value

            if not s[left].isalnum():
                left = left +1
                continue

            if not s[right].isalnum():
                right = right- 1
                continue

            # compare both characters
            if s[left] != s[right]:
                return False

            left = left + 1
            right = right - 1

        return True 
        