from typing import List
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution1:
    def merge2Lists(self,list1:ListNode,list2:ListNode)->ListNode:
        head=ListNode(0)
        cur_node=head
        while list1 and list2:
            if list1.val<list2.val:
                cur_node.next=list1
                list1=list1.next
                cur_node=cur_node.next
            else:
                cur_node.next=list2
                list2=list2.next
                cur_node=cur_node.next
        if list1:
            cur_node.next=list1
        if list2:
            cur_node.next=list2
        return head.next
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        lists_length=len(lists)
        if lists_length==0:
            return None
        if lists_length==1:
            return lists[0]
        mid=lists_length//2
        return self.merge2Lists(self.mergeKLists(lists[:mid]),self.mergeKLists(lists[mid:]))



class PirorList():
    def __init__(self,cmp):
        self.max_length=0
        self.length=0
        self.cmp=cmp
        self.piror_list=[]
    def adjust(self,start,end):
        first_node=self.piror_list[start]
        index=2*start+1
        while index<=end:
            if index<end and self.cmp(self.piror_list[index],self.piror_list[index+1])>0:
                index+=1
            if index<=end and self.cmp(first_node,self.piror_list[index])<0:
                break
            self.piror_list[start]=self.piror_list[index]
            start=index
            index=index*2+1
        self.piror_list[start]=first_node
    def push(self,val):
        if(self.max_length==self.length):
            self.length+=1
            self.max_length+=1
            self.piror_list.append(val)
        elif self.length<self.max_length:
            self.piror_list[self.length]=val
            self.length+=1
        end_node=self.piror_list[self.length-1]
        child_index=self.length-1
        if  child_index<1:
            return 
        parent_index=(child_index-1)//2
        while child_index>0 and self.cmp(end_node,self.piror_list[parent_index])<0:
            self.piror_list[child_index]=self.piror_list[parent_index]
            child_index=parent_index
            if parent_index==0:
                break
            parent_index=(parent_index-1)//2
        self.piror_list[child_index]=end_node

    def pop(self):
        return_val=self.piror_list[0]
        self.piror_list[0]=self.piror_list[self.length-1]
        self.length-=1
        self.adjust(0,self.length-1)
        return return_val

            



class Solution2:
    def cmp(self,node1:ListNode,node2:ListNode):
        return node1.val-node2.val
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        lists_length=len(lists)
        if lists_length==0:
            return None
        if lists_length==1:
            return lists[0]
        piror_list=PirorList(self.cmp)
        for lst in lists:
            piror_list.push(lst)
        head_node=ListNode(0)
        cur_node=head_node
        while piror_list.length>0:
            cur_node.next=piror_list.pop()
            cur_node=cur_node.next
            if cur_node.next:
                piror_list.push(cur_node.next)
        return head_node.next


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
#minheap

class Comparable():
    def __init__(self,lst:ListNode):
        self.lst=lst
        self.val=lst.val
    def __lt__(self,other):
        if self.lst.val>=other.lst.val:
            return False    
        else:
            return True  



class Solution3:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        lists_length=len(lists)
        if lists_length==0:
            return None
        if lists_length==1:
            return lists[0]
        import heapq
        piror_list=[]
        for lst in lists:
            if lst:
                heapq.heappush(piror_list,Comparable(lst))
        head_node=ListNode(0)
        cur_node=head_node
        while len(piror_list)>0:
            cur_node.next=heapq.heappop(piror_list).lst
            cur_node=cur_node.next
            if cur_node.next:
                heapq.heappush(piror_list,Comparable(cur_node.next))
        return head_node.next



class Solution4:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        lists_length=len(lists)
        if lists_length==0:
            return None
        if lists_length==1:
            return lists[0]
        import heapq
        piror_list=[]
        for lst in lists:
            while lst:
                heapq.heappush(piror_list,Comparable(lst))
                lst=lst.next
        head_node=ListNode(0)
        cur_node=head_node
        while piror_list:
            cur_node.next=heapq.heappop(piror_list).lst
            cur_node=cur_node.next
            cur_node.next=None
        return head_node.next


def connect(node1:ListNode,node2:ListNode):
    node1.next=node2
def create_list(arr):
    head=ListNode(0)
    cur=head
    for i in arr:
        node=ListNode(i)
        cur.next=node
        cur=cur.next
    return head.next

def create_lists(lst):
    res=[]
    for i in lst:
        res.append(create_list(i))
    return res

if __name__=='__main__':
    a=[[-1,-1,-1],[-2,-2,-1]]
    #[[-4],[-10,-6,-6],[0,3],[2],[-10,-9,-8,3,4,4],[-10,-10,-8,-6,-4,-3,1],[2],[-9,-4,-2,4,4],[-4,0]]
    b=create_lists(a)
    res=Solution4().mergeKLists(b)
    print(res)