class Solution(object):
    def merge(self, nums1, m, nums2, n):
        
        # Copy nums2 elements into nums1
        for i in range(n):
            nums1[m + i] = nums2[i]
        
        # Sort nums1
        nums1.sort()
        return nums1
