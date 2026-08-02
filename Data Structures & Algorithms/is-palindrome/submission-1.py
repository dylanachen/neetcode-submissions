class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned_s = ''.join([char for char in s if char.isalnum()])
        
        l = 0
        r = len(cleaned_s) - 1

        while l < r:
            if cleaned_s[l].lower() != cleaned_s[r].lower():
                return False
            
            l += 1
            r -= 1
        
        return True
