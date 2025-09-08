# LeetCode 1317. Convert Integer to the Sum of Two No-Zero Integers
# 把1個整數，隨便拆成2個數，就可以了！
# 等等！還有一個條件：拆出來的數，寫成10進位整數時「不能有0藏在裡面」哦！
class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        for i in range(1,n//2+1):  # 暴力去 try 可能的數
            if str(i).count('0')==0 and str(n-i).count('0')==0:
                # 只要「10進位整數」裡「沒有'0'」藏在裡面
                return [i, n-i]  # 就找到答案了！
