# LeetCode 1552. Magnetic Force Between Two Balls 想讓兩兩之間「最小的力」是「最大值」。
# 有點類似「盡量平均分布」。解法「倒過來想」，答案若是dist，能照著放球嗎？ 再用「二分搜尋法」找dist
# 籃子有 10^5 個，籃子 position[i] 介於1...10^9。藍子要放 m 個球，相鄰兩球間的力，剛好是它們的距離
class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        N = len(position)
        position.sort() # 先把座標排序，便知籃子相鄰距離，方便模擬
        def possible(dist)->bool:  # 發明一個函式，用來「測試某個dist距離的可行性」
            prev = position[0] # 第一個球放最左邊
            balls = m - 1 # 剩下 m-1 個球
            for i in range(1, N):
                if position[i]-prev >= dist:  # 照dist距離，可放球
                    prev = position[i]  # 更新
                    balls -= 1  # 更新
                if balls <= 0:
                    return True # 順利放完球，成功，提早結束
            return False  # 沒成功，就是失敗
        # 如果最短距離是left, 可行嗎
        left, right = 1, position[N-1]-position[0]+1
        # 因最少有2顆球，所以最大的距離，是最右籃-最左籃
        while left<right:  # 典型 Binary Search 的寫法
            mid = (left+right) // 2  # 每次切一半
            if possible(mid): # mid可行，距離可再大一些加大
                left = mid + 1
            else:  # mid不可行，當右界
                right = mid
        return left - 1
