class Solution(object):
    def merge(self, nums1, m, nums2, n):
        i,j=m-1,n-1
        for k in range(m+n-1,-1,-1):
            if j<0:
                break
            elif i<0:
                nums1[k]=nums2[j]
                j-=1
            elif nums1[i]<=nums2[j]:
                nums1[k]=nums2[j]
                j-=1
            elif nums1[i]>nums2[j]:
                nums1[k]=nums1[i]
                i-=1
        return nums1