from typing import List
class Solution:
    def findLongestWord(self, s: str, dictionary: List[str]) -> str:
        if not s or len(dictionary)==0:
            return ''
        # dict_lens=[(len(s),index) for index,s in enumerate(dictionary)]
        # dict_lens.sort(reverse=True)
        s_len=len(s)
        res=''
        for word in dictionary:
            dict_len=len(word)
            first=0
            second=0
            while first<s_len and second<dict_len:
                while first<s_len and  s[first]!=word[second]:
                    first+=1
                if first<s_len and s[first]==word[second]:
                    first+=1
                    second+=1
            if second==dict_len:
                if len(res)<dict_len or res>word:
                    res=word
        return res


class Solution2:
    def findLongestWord(self, s: str, dictionary: List[str]) -> str:
        if not s or len(dictionary)==0:
            return ''
        # dict_lens=[(len(s),index) for index,s in enumerate(dictionary)]
        # dict_lens.sort(reverse=True)
        s_len=len(s)
        res=''
        for word in dictionary:
            dict_len=len(word)
            first=0
            second=0
            while first<s_len and second<dict_len:
                while first<s_len and  s[first]!=word[second]:
                    first+=1
                if first<s_len and s[first]==word[second]:
                    first+=1
                    second+=1
            if second==dict_len:
                if len(res)<dict_len or res>word:
                    res=word
        return res

if __name__=='__main__':
    s="abpcplea"
    d=["a","b","c"]
    res=Solution().findLongestWord(s,d)
    print(res)
