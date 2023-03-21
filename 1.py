class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        lst = nums1 + nums2
        n = 0
        lst.sort()
        if len(lst) % 2 == 0:
            n = lst[len(lst)//2] + lst[len(lst)//2 - 1] 
            return n/2
        else:
            return float(lst[len(lst)//2])
            
s = Solution()
print(s.findMedianSortedArrays([1,3],[2]))