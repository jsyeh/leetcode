# LeetCode 72. Edit Distance
# 典型「動態規劃」的問題：word1 要經過「幾次編輯」，會變成 word2
# 編輯包括「插入1個字母、刪掉1個字母、換掉1個字母」
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        @cache
        def helper(i, j):  # 現在處理到 word1[i] vs. word2[j]
            if i==len(word1): return len(word2) - j  # 終止條件 i 走完，剩下全插入
            if j==len(word2): return len(word1) - i  # 終止條件 j 走完，剩下全刪除
            if word1[i]==word2[j]:  # 運氣好、相等，等於「這裡不用編輯」
                return helper(i+1, j+1)  # 可以再問「下面一位」
            # 運氣不好，要試3種不同的編輯方法
            ans1 = helper(i+1,j) + 1  # 方法1: 刪掉 word1[i] 
            ans2 = helper(i,j+1) + 1  # 方法2: 插入 word2[j]
            ans3 = helper(i+1,j+1) + 1  # 方法3: 將 word1[i] 換成 word2[j]
            return min(ans1, ans2, ans3)  # 哪種方法好，就用它
        return helper(0, 0)  # 從 word1[0] word2[0] 開始問
