class Solution(object):
    def maxArea(self, arr):
        left = 0
        right = len(arr)-1
        max_water = 0

        while left < right:
            width = right - left
            height = min(arr[left], arr[right])

            water_area = width * height

            max_water = max(max_water, water_area)

            if arr[left] < arr[right]:
                left += 1
            else:
                right -= 1
       
        return max_water
        