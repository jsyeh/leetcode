class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s2 = ""
        for c in s:
            if c.islower() or c.isnumeric():
                s2 += c
        print(s2)
        N = len(s2)
        for i in range(N//2):
            if s2[i] != s2[N-1-i]: return False
        return True
# case 462/485: "0P" 這個0 isnumeric 所以不能刪，就不是palindrome
