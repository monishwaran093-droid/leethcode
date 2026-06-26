class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        v="aeiou"
        ma=0
        c=0
        for i in range(k):
            if s[i] in v:
                c+=1
        ma=max(c,ma)
        if ma==k:
            return ma
        for j in range(k,len(s)):
            if s[j-k]  in v:
                c-=1
            if s[j]  in v:
                c+=1
            ma=max(c,ma)
            if ma==k:
                return ma
        return ma