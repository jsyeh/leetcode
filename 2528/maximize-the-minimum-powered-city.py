# LeetCode 2528. Maximize the Minimum Powered City
# stations[i] 對應 i城市「有幾個發電站」。
# 每個發電站能服務「左右距離r」的城市，將再建k個發電站，要怎麼建，能讓「最小值」最大？
# 看起來就 binary search 的題目「猜答案」
class Solution:
    def maxPower(self, stations: List[int], r: int, k: int) -> int:
        # 先將 stations 陣列，變成「左邊r增」及「右邊r減」的「增減量」
        N = len(stations)
        diff = [0] * (N+1)
        for i, station in enumerate(stations):
            left, right = max(0, i-r), min(N, i+r+1)
            diff[left] += station
            diff[right] -= station
        
        def helper(ans):  # 我可以再加k個發電場，可達成 ans 的答案嗎？
            nonlocal k
            diff2, k2 = diff[:], k
            now = 0
            for i in range(N):
                now += diff2[i]
                if now < ans:
                    if ans - now > k2:  # 剩下的k全部拿來用，還不夠用
                        return True  # 失敗
                    k2 -= (ans - now)
                    diff2[min(N, i+r*2+1)] -= (ans - now)
                    now = ans
            return False  # 順利巡完全部的答案，成功
        return bisect_left(range(sum(stations)+1+k), True, key=helper) - 1
