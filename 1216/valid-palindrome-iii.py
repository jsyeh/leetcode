# Palindrome 迴文，k-palindrom 是把「k個字母刪掉」後，是迴文
# 感覺像 DP 的問題 dp(i,j,k) 表示現在要判斷 s[i]==s[j] 再縮小
class Solution:
    def isValidPalindrome(self, s: str, k: int) -> bool:
        @cache
        def dp(i, j, k): # 左邊i 右邊j
            if k<0: return False # 用盡k，便失敗
            if i>=j: return True # 如果i,j聚在一起，便是成功
            if s[i]==s[j]: # 頭尾相同
                return dp(i+1, j-1, k) # 便問更簡單的子問題
            # 接下來有兩種可能：刪左邊 or 刪右邊，任一成功即可
            return dp(i+1,j,k-1) or dp(i,j-1,k-1)

        return dp(0,len(s)-1,k) # 最左、最右，開始逐項問
# case 25/51: "bacabaaa" 2

