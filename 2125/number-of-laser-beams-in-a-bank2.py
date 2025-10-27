# LeetCode 2125. Number of Laser Beams in a Bank
# 銀行監控系統，有許多「雷射裝置」，不同 row 間依序會互相射光束。
# 如果整個 row 全空, 就跳過那個row。問總共有幾條光束。
class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        # 找出「有雷射裝置」的每個 row 對應的「雷射裝置」數目
        rows = [row.count('1') for row in bank]  # 先找數量
        rows = [row for row in rows if row > 0]  # 再除掉0
        # 上面「倒裝句」很帥氣，找到「每個 row 的數量」只收 > 0 部分
        ans = 0
        for i in range(len(rows)-1):  # 相鄰兩兩巡一次
            ans += rows[i] * rows[i+1]  # 將相鄰兩個「乘起來」
        return ans
