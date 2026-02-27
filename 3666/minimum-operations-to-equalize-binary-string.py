# LeetCode 3666. Minimum Operations to Equalize Binary String
# 每次可將「二進位字串」挑k個數「0變1、1變0」翻轉，幾次後，可全變成1
class Solution:
    def minOperations(self, s: str, k: int) -> int:
        N = len(s)  # 字串長度 N
        zero = s.count('0')  # 0 的數量，最後希望 zero 數量「都清空」
        if zero==0: return 0  # 無任何0，不需任何flip翻轉，0次翻轉就成功
        if k==N:  # 特殊狀況：只能全部都選，可能成功、可能失敗
            if zero==N: return 1  # 幸運「全部都0」先全選，再flip翻轉1次，成功
            else: return -1  # 不幸運「0和1交錯」就沒辦法達成任務

        ans = []  # 以下模仿 Solutions 裡 Alex Wice （用數學證明後）的速解法
        m1 = ceil(zero/k)  # 條件1：最少要選「幾個k」才能清光
        if zero % 2 == 0:  # 第一種可能：數學證明要翻轉偶數次
            m2 = ceil(zero/(N-k))  # 條件2：翻轉時「不動的N-k個數」為0準備
            if max(m1,m2)%2==0: ans.append( max(m1,m2) )  # 答案必須是偶數
            else: ans.append( max(m1,m2) + 1 )  # 不是偶數，就再+1次，變偶數
        if zero % 2 == k % 2:  # 第二種可能：數學證明要翻轉奇數次
            m2 = ceil((N-zero)/(N-k))  # 條件2：翻轉時「不動的N-k個數」為1準備
            if max(m1,m2)%2==1: ans.append( max(m1,m2) )  # 答案必須是奇數
            else: ans.append( max(m1,m2) + 1 )  # 不是奇數，就再+1次，變奇數
        if len(ans)==0: return -1  # 上面兩種可能
        return min(ans)
  
