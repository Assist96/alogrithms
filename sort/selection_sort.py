
def selection_sort(arr):
    arr_length=len(arr)
    if arr_length<2:
        return arr
    for i in range(arr_length-1):
        min_index=i
        for  j in range(i+1,arr_length):
            if arr[j]<arr[min_index]:
                min_index=j
        if i!=min_index:
            arr[i],arr[min_index]=arr[min_index],arr[i]
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
            print(i)
            return False    
    return  True

def verification(times=2000):
    import random
    for i in range(times):
        arr_len=random.randint(0,times)
        arr=gen_random_list(arr_len)
        arr1=arr.copy()
        res=compare_two_list(arr,arr1)
        arr=selection_sort(arr)
        arr1.sort()
        res=compare_two_list(arr,arr1)
        if not res:
            return False
    return True

if __name__=='__main__':
    # res=selection_sort([8,3,5,8])
    print(verification(500))


