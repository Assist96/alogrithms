from typing import  List
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums1_index=m-1
        nums2_index=n-1
        cur_index=m+n-1
        while nums1_index>=0 and nums2_index>=0:
            if nums1[nums1_index]>nums2[nums1_index]:
                nums1[cur_index]=nums1[nums1_index]
                cur_index-=1
                nums1_index-=1
            else:
                nums1[cur_index]=nums2[nums2_index]
                cur_index-=1
                nums2_index-=1
        while nums2_index>=0:
            nums1[cur_index]=nums2[nums2_index]
            cur_index-=1
            nums2_index-=1

if __name__=='__main__':
    res=Solution().merge([1,2,3,0,0,0],3,[2,5,6],3)
    print(1)