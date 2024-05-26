class Solution:
    def checkRecord(self, s: str) -> bool:
        A, L = 0, 0
        for c in s:
            if c=='A': 
                A += 1
                if A >= 2: return False
            if c=='L':
                L += 1
                if L >= 3: return False
            else:
                L = 0
        return True
