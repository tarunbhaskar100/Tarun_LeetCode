class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        nums[:]= sorted(list(set(nums)))#+['_']*(len(nums)-len(set(nums)))
        return len(set(nums))