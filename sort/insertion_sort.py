
def insertion_sort(arr):
    arr_length=len(arr)
    if arr_length<2:
        return arr
    for i in range(arr_length):
        pre_index=i-1
        cur_val=arr[i]
        while pre_index>=0 and arr[pre_index]>cur_val:
            arr[pre_index+1]=arr[pre_index]
            pre_index-=1
        arr[pre_index+1]=cur_val
    
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
        arr=insertion_sort(arr)
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
    
