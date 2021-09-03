class Solution:
    def reverseVowels(self, s: str) -> str:
        left =0
        right=len(s)-1
        a=['a','e','i','o','u']
        s_lst=list(s)
        while left <=right:
            while left<=right and s_lst[left] not in a:
                left+=1
            while left<=right and s_lst[right] not in a:
                right-=1
            if left>=right:
                break
            s_lst[left],s_lst[right]=s_lst[right],s_lst[left]
            left+=1
            right-=1
        return ''.join(s_lst)

if __name__=='__main__':
    s='leetcode'
    res=Solution().reverseVowels(s)
    print(res)