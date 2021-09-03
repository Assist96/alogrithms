def heap_adjust(arr,start,end):
    firt_num=arr[start]
    index=start*2+1
    while index<=end:
        if index<end  and arr[index]<arr[index+1]:
            index+=1
        if index<=end and  arr[index]<=firt_num:
            break
        arr[start]=arr[index]
        start=index
        index=2*index+1
    arr[start]=firt_num


def build_max_heap(arr):
    arr_length=len(arr)
    index=arr_length//2-1
    while index>=0:
        heap_adjust(arr,index,arr_length-1)
        index-=1


def heap_sort(arr):
    arr_length=len(arr)
    build_max_heap(arr)
    for i in range(arr_length-1,0,-1):
        arr[i],arr[0]=arr[0],arr[i]
        heap_adjust(arr,0,i-1)
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
        arr=heap_sort(arr)
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
