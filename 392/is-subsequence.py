class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = 0 # for t[i]
        for c in s:
            while i<len(t) and t[i] != c:
                i += 1 # 無法正確比對到, 就換下一個
            if i == len(t): # 走到超過範圍, 就表示失敗
                return False
            i += 1 # 迴圈最後, 記得 i增加, 以準備下一輪的比較
        return True
        
