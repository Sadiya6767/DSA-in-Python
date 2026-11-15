class Solution(object):
    def trap(self, arr):
        #Two Pointers
        left = 0
        right = len(arr)-1
        #trapper water assumed
        total_water = 0
        #Two variable to find max container
        max_left = 0
        max_right = 0

        while left < right :
            max_left = max(max_left, arr[left])
            max_right = max(max_right, arr[right])

            if max_left < max_right:
                total_water += max_left - arr[left]
                left += 1
            else:
                total_water += max_right - arr[right]
                right -= 1
        
        return total_water

        