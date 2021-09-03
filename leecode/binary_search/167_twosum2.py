from typing import List
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        num_len=len(numbers)
        left=0
        right=num_len-1
        while (left<right):
            val=numbers[left]+numbers[right]
            if val==target:
                return [left+1,right+1]
            elif val<target:
                left+=1
            elif val>target:
                right-=1
        return [-1,-1]


if __name__=='__main__':
    a=[2,7,11,15]
    res=Solution().twoSum(a,9)
    print(res)