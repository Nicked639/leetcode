# There are two sorted arrays nums1 and nums2 of size m and n respectively.

# Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

# Example 1:
# nums1 = [1, 3]
# nums2 = [2]
# The median is 2.0

# Example 2:
# nums1 = [1, 2]
# nums2 = [3, 4]
# The median is (2 + 3)/2 = 2.5

class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        r = []
        for i in nums1:
            r.append(i)
        for i in nums2:
            r.append(i)
        r.sort()
        print('r = %s'  %r)
        if len(r) == 00:
            return None
        elif len(r) == 1:
            return r[0]
        elif len(r) % 2 != 0:
            return r[(len(r)-1)//2]
        else:
            return (r[len(r)//2]+r[len(r)//2-1])/2.0