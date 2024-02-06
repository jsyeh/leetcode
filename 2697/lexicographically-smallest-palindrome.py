class Solution:
    def makeSmallestPalindrome(self, s: str) -> str:
        s = list(s) # 先轉成 list 方便修改內容
        N = len(s)
        for i in range(N//2): # 頭尾 兩兩比較
            c = min(s[i],s[N-1-i]) # 最小字母c
            s[i] = s[N-1-i] = c # 頭尾都設c
        return ''.join(s) # 變回字串
