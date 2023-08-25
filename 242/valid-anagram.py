class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        H1, H2 = [0]*26, [0]*26
        for c in s:
            i = ord(c) - ord('a')
            H1[i] += 1
        for c in t:
            i = ord(c) - ord('a')
            H2[i] += 1

        for i in range(26):
            if H1[i] != H2[i]: 
                return False
        return True
