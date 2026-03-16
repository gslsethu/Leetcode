class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        list1=nums1+nums2
        list1.sort()
        length=len(list1)

        if length%2==0:
            median=(list1[length//2]+list1[(length//2)-1])/2.0
            return median
        else:
            return list1[length//2]


        