class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1)>len(s2) :
             return False
        f=[0]*26
        f2=[0]*26
        for i in s1:
            f[ord(i)-ord('a')]+=1
        for i  in range(len(s1)):
            f2[ord(s2[i])-ord('a')]+=1
        if f==f2:
            return True
        for i in range(len(s1),len(s2)):
             f2[ord(s2[i])-ord('a')]+=1
             f2[ord(s2[i-len(s1)])-ord('a')]-=1
             if f==f2:
                return True
        return False