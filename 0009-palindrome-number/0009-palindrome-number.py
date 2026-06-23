class Solution:
    def isPalindrome(self, x):
        if x<0:
            return False
        else:
            c=str(x)
            return c[::-1]==str(x)