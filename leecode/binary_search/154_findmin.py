from typing import List
class Solution:
    def findMin(self, nums: List[int]) -> int:
        start=0
        end=len(nums)-1
        while start<=end:
            mid=start+((end-start)>>1)
            if  nums[mid]>nums[end]:
                start=mid+1
            elif nums[mid]<nums[end]:
                end=mid
        return nums[start]

if __name__=='__main__':
    lst=[3,1,2]
    res=Solution().findMin(lst)
    print(res)