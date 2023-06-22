class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        try:
            for i in range(len(nums)):
                nums.remove(val)
        except:
            pass
        return len(nums)
