class Solution:
    def reverseVowels(self, s: str) -> str:
        s=list(s)
        a="aeiouAEIOU"
        i=0
        j=len(s)-1
        while(i<j):
            if s[i] in a and s[j] in a:
                s[i],s[j]=s[j],s[i]
                i+=1
                j-=1
            elif s[i] not in a:
                i+=1
            elif s[j] not in a:
                j-=1
        return("".join(s))
