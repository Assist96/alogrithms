from typing import List
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res=[]
        for first in range(len(nums)-2):
            if nums[first]>0:
               break
            if first >0 and nums[first]==nums[first-1]:
                continue
            second,third=first+1,len(nums)-1
            while second<third:
                sum=nums[first]+ nums[second]+nums[third]
                if sum==0:
                    res.append([nums[first],nums[second],nums[third]])
                    second+=1
                    third-=1
                    while second<third and  nums[second]==nums[second-1]:
                        second+=1
                    while  second<third and  nums[third]==nums[third+1]:
                        third-=1
                elif sum>0:
                    third-=1
                    while  second<third and  nums[third]==nums[third+1]:
                        third-=1
                elif sum<0:
                    second+=1
                    while second<third and  nums[second]==nums[second-1]:
                        second+=1
               
        return  res


if __name__=='__main__':
    a=[-1,0,1,2,-1,-4]
    res=Solution().threeSum(a)
    print(res)