class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
     c=[]
     for i in range(len(accounts)):
            c.append(sum(accounts[i]))
     return max(c)