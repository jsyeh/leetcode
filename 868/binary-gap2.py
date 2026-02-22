# LeetCode 868. Binary Gap
# 整數 n 以二進位表示，想找「兩個1之間」最大距離
class Solution:
    def binaryGap(self, n: int) -> int:
        ans = zeros = 0  # 找「連續幾個0」
        bits = bin(n)  # 變成 '0b1...' 的字串型式
        # 因 1<=n 所以一定有第1個'1'在bits[2]
        for i in range(3, len(bits)):  # 從bits[3]開始
            if bits[i]=='0':  # 遇到'0'
                zeros += 1  # 「連續幾個0」的數目+1
            else:  # 遇到 '1' 便與前面的'1'有間隔
                ans = max(ans, zeros+1)  # 更新答案
                zeros = 0  # 新的'1'、「連續幾個0」新的開始
        return ans
