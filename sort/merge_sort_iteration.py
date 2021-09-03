def merge_sort_iteration(arr):
    arr_length=len(arr)
    i=1
    while i<arr_length:
        left_start=left_end=right_start=right_end=0
        while left_start<=arr_length-i:
            merged=[]
            right_start=left_end=left_start+i
            right_end=left_end+i
            if right_end>arr_length:
                right_end=arr_length
            left=arr[left_start:left_end]
            right=arr[right_start:right_end]
            while left and right:
                if left[0]<=right[0]:
                    merged.append(left.pop(0))
                else:
                    merged.append(right.pop(0))
            
            merged.extend(left if  left else right)
            arr[left_start:right_end]=merged
            left_start+=i*2
        i*=2
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
        arr=merge_sort_iteration(arr)
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
    