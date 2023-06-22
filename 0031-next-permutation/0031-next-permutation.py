class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums_sort = nums.copy()
        nums_sort.sort(reverse=True)
        if nums_sort == nums:
            nums.sort()
        else:
            def max_th(nu):
                di = nu[0]
                nu.sort(reverse=True)
                re = nu[nu.index(di)-1]
                nu.remove(re)
                nu.sort()
                # print(re , nu)
                return [re]+nu
            for i in range(-1,-len(nums),-1):
                if nums[i] > nums[i-1]:
                    nums[:] = nums[:i-1]+max_th(nums[i-1:])
                    break