class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p)>len(s):
           return [] 
        f=[0]*26
        f2=[0]*26
        c=[]
        for i in p:
            f[ord(i)-ord('a')]+=1
        k=len(p)
        for i in range(k):
            f2[ord(s[i])-ord('a')]+=1
        if f==f2:
            c.append(0)
        for i in range(k,len(s)):
            f2[ord(s[i])-ord('a')]+=1
            f2[ord(s[i-k])-ord('a')]-=1
            if f==f2:
                c.append(i-k+1)
        return c