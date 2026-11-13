class Solution(object):
    def twoSum(self, nums, target):
        nums = sorted((val, i) for i, val in enumerate(nums))

        left = 0 
        right = len(nums) - 1

        while left < right:
            total = nums[left][0] + nums[right][0]

            if total == target:
                return [nums[left][1], nums[right][1]]

            elif total < target:
                left = left + 1

            else:
                right = right - 1

        return []
