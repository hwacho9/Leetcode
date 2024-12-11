class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        
        left = 0
        sub = 0
        
        while left < len(s) and sub < len(t):
            if s[left] == t[sub]:
                left += 1
            sub += 1
            
        return left == len(s)
                
            
            