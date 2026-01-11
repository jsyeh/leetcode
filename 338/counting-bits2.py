# LeetCode 338. Counting Bits
# 將 0...n 的每個數，都用「二進位表示」，再記錄裡面「對應的1有幾個」
class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = []
        for i in range(n+1):
            ans.append(bin(i).count('1'))
        return ans
