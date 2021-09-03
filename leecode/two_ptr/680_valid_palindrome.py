class Solution:
    def judge(self,s,left,right,deleted):

        while left<right:
            if s[left]==s[right]:
                left+=1
                right-=1
            elif  not deleted:
                return self.judge(s,left+1,right,True) or self.judge(s,left,right-1,True)
            else:
                return False
        return True
    def validPalindrome(self, s: str) -> bool:
        s_len=len(s)
        if s_len<2:
            return True
        left=0
        right=len(s)-1
        deleted=False
        return self.judge(s,left,right,deleted)

if __name__=='__main__':
    s="abc"
    res=Solution().validPalindrome(s)
    print(res)