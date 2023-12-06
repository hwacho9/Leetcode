class Solution:
    def isPalindrome(self, x: int) -> bool:
        n = list(map(str, str(x)))
        r = list(map(str, str(x)))
        r.reverse()
        if (r == n):
            return True
        else:
            return False