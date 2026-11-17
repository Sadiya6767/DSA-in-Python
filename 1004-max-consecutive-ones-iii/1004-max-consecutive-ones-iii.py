class Solution(object):
    def longestOnes(self, nums, k):
        left = 0
        right = 0
        count_zeros = 0
        max_len = 0

        while right < len(nums):
            if nums[right] == 0:
                count_zeros +=1 

            while count_zeros > k:
                if nums[left] == 0:
                    count_zeros -= 1

                left += 1

            max_len = max(max_len , right - left + 1)

            right += 1

        return max_len
        