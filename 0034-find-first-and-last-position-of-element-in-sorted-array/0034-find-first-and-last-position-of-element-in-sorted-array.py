class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if target in nums:
            
            s = nums.index(target)
            if nums[-1] != target:
                for i in range(s,len(nums)):
                    if nums[i] != target:
                        break
                return [s,i-1]
            else:
                return [s,len(nums)-1]
        else:
            return [-1,-1]