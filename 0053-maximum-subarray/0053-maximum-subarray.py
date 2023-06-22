class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        out = nums[0]
        cu_max = 0
        for i in nums:
            cu_max = max(cu_max,0)
            cu_max += i
            out = max(out,cu_max)
        return out