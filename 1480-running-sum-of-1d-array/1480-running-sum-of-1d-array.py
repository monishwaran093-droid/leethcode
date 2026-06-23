class Solution:
    def runningSum(self, nums: List[int]):
          t=0
          d=[]
          for i in range(len(nums)):
            t+=nums[i]
            d.append(t)
          return d