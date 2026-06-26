class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        s=0
        c=0
        for i in range(k):
            s+=arr[i]
        if s//k >=threshold:
            c+=1
        for j in range(k,len(arr)):
            s=s-arr[j-k]
            s=s+arr[j]
            if s//k>=threshold:
                c+=1
        return c