# LeetCode 386. Lexicographical Numbers
# 將 1...n 的全部數字，「以字母序」排序好
class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        # for i in range(1,n+1):  # 將1...n逐一列出，原本 for 迴圈長這樣
        a = [str(i) for i in range(1,n+1)]  # 用倒裝句，產生全部數字的字串
        a.sort()  # 再將字串「以字母序」排序好
        ans = [int(n) for n in a]  # 用倒裝句，將排好的數字字串，轉成int整數
        return ans
        
