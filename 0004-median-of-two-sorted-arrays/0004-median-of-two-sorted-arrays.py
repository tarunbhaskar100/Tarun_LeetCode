class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums1 = nums1+nums2
        nums1.sort()
        if len(nums1)%2 == 1:
            return float(nums1[len(nums1)//2])
        else:
            a = len(nums1)//2
            return float(sum(nums1[a-1:a+1])/2)