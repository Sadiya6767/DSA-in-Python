class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        left = 0
        right = 0
        max_count = 0

        while right < len(nums):

            if nums[right] == 0:
                left = right + 1

            else:
                max_count = max(max_count, right - left + 1)

            right += 1

        return max_count