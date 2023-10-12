# 這題比較難，因為「竟然只能用現有的 list 的記憶體」，搬動就要想想
# 我想到的方法有點亂。
# 後來看了Editorial 的解法，就頭尾逐一交換，再每次逐一交換，有夠帥的
class Solution:
    def reverseWords(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        N = len(s)
        for i in range(N//2): # 長度的一半，做交換
            s[i], s[N-1-i] = s[N-1-i], s[i]
        # 前面頭尾逐一交換
        # 下面再逐字逐一交換
        left = 0
        for i in range(N+1): # 多一格，希望簡化下面交換的程式碼（只寫一次）
            if i==N or s[i] == ' ': # 遇到空格 or 整個結尾，就交換
                N2 = i - left # 小字的長度
                for k in range(N2//2): # 長度的一半，做交換
                    s[left+k], s[i-1-k] = s[i-1-k], s[left+k]
                left = i + 1
        return s 
        
