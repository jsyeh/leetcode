# 變形的 palindrome迴文，可接受「刪1個字母」
# 即第1次「比對錯誤」時，可以「刪左」或「刪右」修正
class Solution:
    def validPalindrome(self, s: str) -> bool:
        N = len(s)
        for i in range(N//2):
            if s[i] != s[N-1-i]: # 第1次比對錯誤
                # 有1次可以「刪字母」的修正機會
                # 有兩種可能的修正法：忽視 s[i] 或 s[N-1-i]
                delLeft = s[i+1:N-1-i+1]
                delRight = s[i:N-1-i]
                if delLeft==delLeft[::-1]: # 第一種成功的可能性
                    return True
                if delRight==delRight[::-1]: # 第二種成功的可能
                    return True
                # 前兩種都沒成功，就失敗了
                return False
        return True # 沒有任何錯誤的比對結束，很好
