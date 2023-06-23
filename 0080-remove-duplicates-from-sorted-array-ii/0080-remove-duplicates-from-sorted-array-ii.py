class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        out = []
        for i in sorted(list(set(nums))):
            if nums.count(i) >= 2:
                out += [i]*2
            else:
                out.append(i)
        nums[:] = out + ['_']*(len(nums)-len(out))
        return len(out)