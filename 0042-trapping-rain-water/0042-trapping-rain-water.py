class Solution:
    def trap(self, height: List[int]) -> int:
        water_trapped = 0
        # define the size
        size = len(height)
        # define the left and right max
        left_max = 0
        right_max = 0
        # define the left and right pointer
        left = 0
        right = size - 1
        # iterate over the height
        while left <= right:
            # check the condition
            if height[left] <= height[right]:
                # check the condition
                if height[left] >= left_max:
                    # update the left max
                    left_max = height[left]
                else:
                    # update the water trapped
                    water_trapped += left_max - height[left]
                # increment the left
                left += 1
            else:
                # check the condition
                if height[right] >= right_max:
                    # update the right max
                    right_max = height[right]
                else:
                    # update the water trapped
                    water_trapped += right_max - height[right]
                # decrement the right
                right -= 1
        # return the water trapped
        return water_trapped