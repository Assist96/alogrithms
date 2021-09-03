def radix_sort(arr):
    radix=0
    arr_len=len(arr)
    if arr_len<2:
        return arr
    max_num=max(arr)
    max_radix=len(str(max_num))
    while radix<max_radix:
        buckets=[[] for _ in range(10)]
        for item in arr:
            buckets[(item//10**max_radix)%10].append(item)
        arr.clear()
        for bucket in buckets:
            if bucket:
                arr.extend(sorted(bucket))
        max_radix+=1
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
        arr=radix_sort(arr)
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
