from typing import List


class ListNode:
    def __init__(self,val=0,next=None):
        self.val=val
        self.next=next

def list_insert_sorted(head_node,node):
    cur_node=head_node
    next_node=cur_node.next
    while next_node:
        if node.val >next_node.val:
            cur_node=next_node
            next_node=cur_node.next
        else:
            cur_node.next=node
            node.next=next_node
            break
    if not next_node:
        cur_node.next=node

def get_bucket_item(bucket):
    res_list=[]
    head=bucket
    next_node=head.next
    while next_node:
        res_list.append(next_node.val)
    return res_list

def merge_bucket(head1,head2):
    next1=head1.next
    next2=head2.next
    cur_node=head1
    while next1 and next2:
        if(next1.val<next2.val):
            cur_node.next=next1
            next1=next1.next
            cur_node=cur_node.next
        else:
            cur_node.next=next2
            next2=next2.next
            cur_node=cur_node.next
    if next1:
        cur_node.next=next1
    if next2:
        cur_node.next=next2
    return head1

def bucket_sort(arr,n=110):
    buckets=[ListNode() for _ in range(n)]
    arr_length=len(arr)
    for i in range(arr_length):
        bucket_index=arr[i]%n
        bucket_node=ListNode(arr[i])
        bucket_head=buckets[bucket_index]
        list_insert_sorted(bucket_head,bucket_node)
    merged_head=buckets[0]
    for i in range(1,n):
        merged_head=merge_bucket(merged_head,buckets[i])
    next_node=merged_head.next
    for i in range(arr_length):
        arr[i]=next_node.val
        next_node=next_node.next
    return arr

def bucket_sort_2(arr):
    arr_length=len(arr)
    if(arr_length<2):
        return arr
    min_num=min(arr)
    max_num=max(arr)
    bucket_range=(max_num-min_num)/arr_length
    if bucket_range==0:
        return arr
    buckets=[[] for _ in range(arr_length+1)]
    for item in arr:
        buckets[int((item-min_num)//bucket_range)].append(item)
    arr.clear()
    for bucket in buckets:
        arr.extend(sorted(bucket))
    return arr

def connect_node(node1,node2):
    node1.next=node2


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
        arr=bucket_sort_2(arr)
        arr1.sort()
        res=compare_two_list(arr,arr1)
        if not res:
            return False
    return True


if __name__=='__main__':
    import time
    st=time.time()
    # res=bucket_sort([29,25,3,49,9,37,21,43])
    print(verification(5000))
    print(time.time()-st)


