# LeetCode 2406. Divide Intervals Into Minimum Number of Groups
# 撞在一起的 intervals 要分在不同群，問「最小」有分幾群即可。
# Hint 2 暗示「最多重疊的數量」就是答案。有點像「開會需要幾間會議室」
# 昨天題目「朋友來訪」坐椅子，簡化成「記錄最多用了幾個椅子」就解決了
class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        intervals.sort()  # 照 left 時間排序（left開始,right離開）
        heap = []  # 記錄目前使用中的會議室「離開時間」
        ans = 0
        for left, right in intervals:  # 照left開始時間，依序處理
            while len(heap)>0 and heap[0]<left:  # 若有會議室可「先歸還」
                heappop(heap)  # 將會議室「先歸還」
            heappush(heap, right)  # 「借1間會議室」記錄right「離開時間」
            ans = max(ans, len(heap))  # 更新「會議室」要幾間
        return ans
