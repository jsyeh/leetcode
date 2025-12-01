# LeetCode 2141. Maximum Running Time of N Computers
# n台電腦，由m個不同電量的電池供電，希望同時持續開機。
# 每個電池可供電 batteries[i] 分鐘的電，可瞬間切換電池，最多可撐幾分鐘。
# 我使用 lee215 的解法：運氣好的話，平均=total/n 是答案。但若 max()>平均，那就會浪費掉
# 會浪費掉/用不完的電池，專屬某台電腦。新平均=剩下的電量量/剩下的電腦量，持續做下去即可
class Solution:
    def maxRunTime(self, n: int, batteries: List[int]) -> int:
        B = sorted(batteries, reverse=True)  # 變數名太長了，改叫 B 電池容量，大到小排好
        total = sum(B)  # 總電量（總電量/n，運氣好可能是答案，但要扣掉「浪費的電」）
        for i in range(len(B)):
            if B[i]>total/n:  # 目前電量最大的電池，比現在的平均大，浪費掉
                total -= B[i]  # 就不要考慮這顆電池了，它專門用一台電腦
                n = n - 1  # 不要管那台「專門用」的電腦，考慮「剩下的電腦」
            else: # 電量最大的電池，不會「電量用不完、浪費掉」太幸運了！
                return total // n  # 接下來就沒有任何電池會浪費掉，可全部平均用光
