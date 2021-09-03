def partion(arr,low,high):
    povit_num=arr[low]
    index=low+1
    i=index
    while low<high:
        while low <high and arr[high]>=povit_num :
            high-=1
        arr[low]=arr[high]
        while low<high and  arr[low]<=povit_num:
            low+=1
        arr[high]=arr[low]
    arr[low]=povit_num
    return low

def quick_sort(arr,low=0,high=None):
    if   high is None:
        high=len(arr)-1
    if(low<high):
        pivot=partion(arr,low,high)
        quick_sort(arr,low,pivot-1)
        quick_sort(arr,pivot+1,high)
    return arr


def gen_random_list(len=10):
    import random
    random_lst=[]
    for i in range(len):
        random_lst.append(random.randint(0,len*2))
    return random_lst

def compare_two_list(lst1,lst2):
    lst1_len=len(lst1)
    lst2_len=len(lst2)
    if lst1_len!=lst2_len:
        return False
    for i in range(lst1_len-1):
        if(lst1[i]!=lst2[i]):
            return False    
    return  True

def verification(times=2000):
    import random
    for i in range(times):
        arr_len=random.randint(0,times)
        arr=gen_random_list(arr_len)
        arr1=arr.copy()
        arr=quick_sort(arr)
        arr1.sort()
        res=compare_two_list(arr,arr1)
        if not res:
            return False
    return True


if __name__=='__main__':
    import time
    st=time.time()
    print(verification(500))
    print(time.time()-st)

    # res=quick_sort([1,4,9,2,5,7,3,5])
    # print(res)