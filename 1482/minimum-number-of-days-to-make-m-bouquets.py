# 想知幾天後，開出來的花，才夠做出 m 個花束（每個花束需採相鄰k朵花）
# 要用暴力法去模擬花開會超時，也不能用 sort 因為要查看花的位置
# 所以用 binary search 看 day mid 開的花夠不夠用
class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        N = len(bloomDay)
        def possible(day: int) -> bool: # 請問第day天，開的花夠用嗎？
            flower = 0 # 目前有連續幾朵花
            bouquet = 0 # 目前做出幾個花束（每束花需連續k朵花）
            for i in range(N): # 去查每朵花有沒有開
                if bloomDay[i]<=day: # 如果花有開的話
                    flower += 1 # 多了1朵花能用
                    if flower >= k: # 花連續湊齊k朵
                        bouquet += 1 # 就多1個花束
                        flower -= k # 並用掉k朵花
                        if bouquet >= m: return True # 湊齊 m 花束，成功
                else: # 這裡花沒開的話
                    flower = 0 # 花又歸零了
            return False # 離開迴圈時，還沒有收齊足夠多的花束
        
        left, right = 1, max(bloomDay)+1 # 右不包含：這天花全開，還不夠
        while left < right:
            mid = (left+right)//2
            if not possible(mid): # 這天花不夠的話
                left = mid + 1 # 就左邊界再多1天
            else:
                right = mid # 右邊界設在這裡，繼續逼近

        if left>max(bloomDay): return -1 # 結束時，如果全開也不夠，就失敗
        else: return left

