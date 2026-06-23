class Solution:
    def isPalindrome(self, s: str) -> bool:
            sr=""
            for  i in s:
                    if i.isalnum():
                        sr+=i.lower()
            if sr=="" or sr==sr[::-1]:
                return True
            return False