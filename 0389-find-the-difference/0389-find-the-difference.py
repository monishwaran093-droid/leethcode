class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        mp={}
        for ch in t:
            mp[ch]=mp.get(ch,0)+1
        for ch in s:
            mp[ch]-=1
        for ch in mp:
            if mp[ch]>0:
                return ch