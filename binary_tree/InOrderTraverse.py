class BTree():
    def __init__(self,val,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right


def InOrderTraverse(root:BTree):
    stack=[]
    cur=root
    res=[]
    while cur or not stack:
        stack.append(cur)
        if cur.left:
            cur=cur.left
        else:
            last=stack.pop()
            res.append(last)
            cur=last.right
    return res

def create_BTree(root,lst,index=0):
    if index<len(lst):
        if   not lst[index] :
            return None,index+1
        else:
            root=BTree(lst[index])
            index+=1
            root.left,index=create_BTree(root.left,lst,index)
            root.right,index=create_BTree(root.right,lst,index)
            return root,index
    return root,index

if __name__=='__main__':
    lst=[1,2,3,None,None,4,5,None,6]
    root=BTree(0)
    root,index=create_BTree(root,lst)
    print(1)