from typing import List
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        nums_length=len(nums)
        if nums_length<4:
            return []
        nums.sort()
        res=[]
        for first in range(nums_length-3):
            if (nums[first]>target):
                break
            if first>0 and nums[first]==nums[first-1]:
                continue
            for second in range(first+1,nums_length-2):
                if second>first+1 and  nums[second]==nums[second-1]:
                    continue
                if (nums[second]>target):
                    break
                third=second+1
                fourth=nums_length-1
                while third<fourth:
                    sum=nums[first]+nums[second]+nums[third]+nums[fourth]
                    if sum==target:
                        res.append([nums[first],nums[second],nums[third],nums[fourth]])
                        third+=1
                        fourth-=1
                        while third<fourth and nums[third]==nums[third-1]:
                            third+=1
                        while third<fourth and nums[fourth]==nums[fourth+1]:
                            fourth-=1
                    elif sum>target:
                        fourth-=1
                        while third<fourth and nums[fourth]==nums[fourth+1]:
                            fourth-=1
                    elif sum<target:
                        third+=1
                        while third<fourth and nums[third]==nums[third-1]:
                            third+=1
        return res

if __name__=='__main__':
    res=Solution().fourSum([-1,0,1,2,-1,-4],-1)
    print(res)