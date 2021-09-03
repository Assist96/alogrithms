def mySqrt(x:int)->int:
    if x<2:
        return x
    start=0
    end=x
    res=-1
    while start<=end:
        mid=start+((end-start)>>1)
        val=mid*mid
        if val==x:
            return mid
        elif val<x:
            start=mid+1
        elif val>x:
            end=mid-1
    if end!=start-1:
        print('True')
    return start-1

def test(n=50000):
    import random
    import math
    for i in range(n):
        random_val=random.randint(0,2*n)
        target_val=int(math.sqrt(random_val))
        mySqrt_val=mySqrt(random_val)
        if target_val!=mySqrt_val:
            print(f'target :{target_val}|myVal:{mySqrt_val}')
            return False
    
    return True

if __name__=='__main__':
    re1=mySqrt(11)
    re2=mySqrt(10)
    res=test()
    print(res)