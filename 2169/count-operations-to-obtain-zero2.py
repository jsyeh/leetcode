# LeetCode 2169. Count Operations to Obtain Zero
# 如果 num1 >= num2 就讓 num1 -= num2
# 否則 num2 -= num1
# 看何時會得到0。照著規則模擬即可
class Solution:
    def countOperations(self, num1: int, num2: int) -> int:
        ans = 0
        while num1 != 0 and num2 != 0:  
            # 題目希望「任一個為0」所以「都不為0」就一直做
            if num1 >= num2:  # 題目說，「大的」要被「小的」減掉
                # 就像「輾轉相除法」會比「一直做減法」快，能用「除數、餘數」加速嗎？
                ans += num1 // num2  # 除法知道「要做幾次減法」
                num1 %= num2  # 直接變成餘數
            else:
                ans += num2 // num1  # 除法知道「要做幾次減法」
                num2 %= num1  # 直接變成餘數
        return ans
