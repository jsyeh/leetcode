# LeetCode 1482. Minimum Number of Days to Make m Bouquets
# 花園裡的花，會照著bloomDay開花。連續k朵花，可以綁成1個花束。
# 問要過幾天，才能湊齊m個花束。用暴力法模擬花開會超時，也不能用 sort 因為要查看花的位置。
# 所以用 binary search 看 哪一天 開的花夠用。
class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if len(bloomDay)<k*m: return -1 # 全部的花開「卻」還不夠用，失敗！
        def possible(day: int) -> bool: # 請問第day天，開的花夠用嗎？
            flower = 0 # 目前「連續」幾朵花
            bouquet = 0 # 目前做出幾個花束（每束花需連續k朵花）
            for d in bloomDay: # 去查每朵花有沒有開
                if d<=day: # 這朵花在指定day之前「就開花了」
                    flower += 1 # 多了1朵（連續的）花能用
                else: # 這裡花沒開的話，做一次「更新/檢查」
                    bouquet += (flower // k)  # 目前連續的flower能綁幾束花
                    if bouquet>=m: return True  # 湊齊 m 花束，成功
                    flower = 0 # 花又歸零了
            # 離開迴圈時，再做一次「更新/檢查」
            bouquet += (flower // k)  # 目前連續的flower能綁幾束花
            if bouquet>=m: return True  # 湊齊 m 花束，成功
            return False # 離開迴圈時，還沒有收齊足夠多的花束，失敗
        left, right = min(bloomDay), max(bloomDay)  # 二分法，用 left, right 範圍
        while left < right:  # Binary Search 的典型作法，像猜數字一樣，還有夾到範圍
            mid = (left+right)//2  # 先猜中間的數
            if not possible(mid): # 這天花不夠的話
                left = mid + 1 # 就左邊界再多1天，希望夠用，繼續逼近
            else:  # 花夠用的話
                right = mid # 右邊界設在這裡，繼續逼近
        return left

