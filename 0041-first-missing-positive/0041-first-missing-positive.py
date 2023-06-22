class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums = list(set(nums))
        import numpy
        neg_count = len(list(filter(lambda x: (x <= 0), nums)))
        nums.sort()
        nums = nums[neg_count:]
        if len(nums) > 0:
            if nums[0] == 1:
                if len(nums) == 1 or nums[1] != 2:
                    return 2
                data = list(numpy.array(nums[1:]) - numpy.array(nums[:-1]))
                l=[]
                for i in set(data):
                    l.append(data.index(i))
                l.sort()
                    
                if max(data) != 1: 
                    ans = nums[0]+ l[1]+1
                    return ans
                else:
                    return nums[-1]+1
            else:
                return 1
        else:
            return 1