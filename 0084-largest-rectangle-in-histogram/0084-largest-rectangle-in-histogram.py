class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []#deque()
        # define the maximum area
        maximum_area = 0
        # define the index
        index = 0
        # iterate over the heights
        while index < len(heights):
            # check the condition
            if (not stack) or (heights[stack[-1]] <= heights[index]):
                # append the index
                stack.append(index)
                # increment the index
                index += 1
            else:
                # pop the element
                top = stack.pop()
                # calculate the area
                area = (heights[top] * ((index - stack[-1] - 1) if stack else index))
                # update the maximum area
                maximum_area = max(maximum_area, area)
        # iterate over the stack
        while stack:
            # pop the element
            top = stack.pop()
            # calculate the area
            area = (heights[top] * ((index - stack[-1] - 1) if stack else index))
            # update the maximum area
            maximum_area = max(maximum_area, area)
        # return the maximum area
        return maximum_area