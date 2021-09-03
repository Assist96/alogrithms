def counting_sort(arr,maxVal):
    bucketLen=maxVal+1
    bucket=[0]*bucketLen
    arr_length=len(arr)
    for i in range(arr_length):
        bucket[arr[i]]+=1
    index=0
    for i in range(bucketLen):
        while bucket[i]>0:
            arr[index]=bucket[i]
            index+=1
            bucket[i]-=1
    return   arr
    