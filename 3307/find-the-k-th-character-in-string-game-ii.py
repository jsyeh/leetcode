# LeetCode 3307. Find the K-th Character in String Game II
# 字串長度會一直加倍，operations[i] 分成 0:copy, 1: copy加1
# 要找到第 k 個字母，但 k 超級大，所以絕對不能暴力產生全部的字串
# 照 lee215 的建議，直接分析 0-index k 的二進位值，再對 operations[i] 來修正答案
class Solution:
    def kthCharacter(self, k: int, operations: List[int]) -> str:
        k -= 1  # 改成 0-index
        bits = []
        while k>0:  # 用剝皮法，找出二進位值
            bits.append(k%2)  # 由「低位到高位」
            k //= 2  # 慢慢把皮剝完
        shift = 0  # 字母 'a' 在複製時，會「位移」+1幾次
        for i in range(len(bits)):
            if bits[i]==1:  # 當二進位對應1有值時
                shift += operations[i]  # 看是否有+1
        return chr(ord('a') + shift%26)  # 印出shift位移循環後的字母
        
