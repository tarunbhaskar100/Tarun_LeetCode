class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0:
            return [[]]
        if len(nums) == 1:
            return [[], nums]
        return self.subsets(nums[1:]) + [[nums[0]] + i for i in self.subsets(nums[1:])]