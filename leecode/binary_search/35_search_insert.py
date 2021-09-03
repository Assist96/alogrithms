from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        nums_len=len(nums)
        start=0
        end=nums_len-1
        while start<=end:
            mid=start+((end-start)>>1)
            val=nums[mid]
            if val==target:
                return mid
            elif val >target:
                end=mid-1
            elif val<target:
                start=mid+1
        return start

def gen_random_list_sorted(len=10):
    import random
    random_lst=[]
    for i in range(len):
        random_lst.append(random.randint(0,len*2))
    random_lst.sort()
    return random_lst


def verification(times=2000):
    import random 
    for i in range(times):
        arr_len=random.randint(0,times)
        arr=gen_random_list_sorted(arr_len)
        target=random.randint(0,arr_len)
        res1=Solution().searchInsert(arr,target)
        target_res=sum([x<=target for x in arr])
        if target_res>0 and target_res<arr_len:
            target_res-=1
        if  res1!=target_res:
            return False
    return True

if __name__=='__main__':
    res=verification(10)
    print(res)