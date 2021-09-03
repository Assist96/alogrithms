from typing import List
class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        start=0
        end=len(letters)-1
        if target<letters[0]:
            if ord(letters[0])-ord(target)<ord('z')-ord(letters[end])+ord(target)-ord('a'):
                return letters[0]
            else:
                return letters[end]
        if target>letters[end]  :
            if ord(target)-ord(letters[end])<ord('z')-ord(target)+ord(letters[0])-ord('a'):
                return letters[0]
            else:
                return letters[end]
        while start<=end:
            mid=start+((end-start)>>1)
            if letters[mid]==target:
                return letters[mid+1]
            elif letters[mid]>target:
                end=mid-1
            elif letters[mid]<target:
                start=mid+1
        return letters[start]

if __name__=='__main__':
    letters=["c","f","j"]
    target='a'
    res=Solution().nextGreatestLetter(letters,target)
    print(res)