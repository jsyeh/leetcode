# 如果 num1 >= num2 就讓 num1 -= num2
# 否則 num2 -= num1
# 看何時會得到0。就照著規則模擬即可
class Solution:
    def countOperations(self, num1: int, num2: int) -> int:
        ans = 0
        while num1!=0 and num2!=0: # 都還不是0
            if num1 >= num2: num1 -= num2
            else: num2 -= num1
            ans += 1
        return ans
