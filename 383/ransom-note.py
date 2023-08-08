class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        chars = {}
        for c in magazine:
            if c in chars:
                chars[c] += 1
            else:
                chars[c] = 1
        
        for c in ransomNote:
            if c in chars and chars[c]>0:
                chars[c] -= 1
            else:
                return False
        return True
