# int(num[i]) 對應 數字 i 在 num字串裡出現的次數
# 請寫程式確認是否如此
class Solution:
    def digitCount(self, num: str) -> bool:
        N = len(num)
        count = defaultdict(int)
        for i in range(N):
            count[int(num[i])] += 1 # 統計每個字母出現的次數
        for i in range(N): # 再逐項檢查是否成立
            if int(num[i])!=count[i]: return False # 不成立
        return True # 都成立
