# LeetCode 2145. Count the Hidden Sequences
# differences 有相鄰數字的差 hidden[i+1] - hidden[i]
# 希望 hidden 介於 lower ... upper 範圍內，有幾種可能的 hidden 陣列？
class Solution:
    def numberOfArrays(self, differences: List[int], lower: int, upper: int) -> int:
        now = nowLower = nowUpper = 0  # 用來模擬的 now 及對應的 lower upper 範圍
        for d in differences:  # 從 0 開始，依序模擬「加加減減」的過程
            now += d  # 更新 now
            nowLower = min(nowLower, now)  # 更新 now 模擬時的下界
            nowUpper = max(nowUpper, now)  # 更新 now 模擬時的上界
        nowR = nowUpper - nowLower  # now 模擬時的範圍
        r = upper - lower  # 題目希望的範圍
        if r < nowR: return 0  # 若不幸模擬範圍太大、無法塞入題目範圍，就失敗
        return r - nowR + 1  # 可以塞入題目範圍「滑動」的話，算出對應「滑動範圍」的各種可能
