# LeetCode 762. Prime Number of Set Bits in Binary Representation
# 在 left ... right 範圍，有幾個整數的二進位表示的1的數量是質數
# 數字 < 10^6，對應的二進位有20位，所以質數為{2,3,5,7,11,13,17,19}
class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        ans = 0
        prime = {2,3,5,7,11,13,17,19}  # 快速找質數的對照表
        for i in range(left, right+1):  # 在 left ... right 範圍內
            if bin(i).count('1') in prime:  # 若1的數量是質數
                ans += 1  # 找到一個
        return ans
