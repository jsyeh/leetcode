# LeetCode 2163. Minimum Difference in Sums After Removal of Elements
# nums 原有 3*n 個數，刪掉 n 個數後，剩的「前n個數相加」減「後n個數相加」要最小
# 希望「左邊小、右邊大」，直覺策略：「刪掉前面大的」or「刪掉後面小的」但討論區一堆人哇哇叫
# Noah 分享用heap解，Bakerston 圖解左邊 max-heap 吐掉大的(才會最小)右邊 min-heap 吐掉小的(才會最大)
class Solution:
    def minimumDifference(self, nums: List[int]) -> int:
        n = len(nums) // 3  # 總長是 3*n
        preSum, postSum = 0, 0  # 對應左邊 n 個 sum、右邊 n 個 sum
        heap1, heap2 = [], []  # 對應左邊 max-heap(吐大的，才會小)、右邊 min-heap(吐小的，才會大)
        # 左邊的 n 個 ==================
        for i in range(n): # 左邊的 preSum
            preSum += nums[i]  # 左邊 sum
            heappush(heap1, - nums[i])  # 左邊 max-heap（用負的）
        # 左邊「每次都吐掉」最大的，便能留下「最小的n個」
        table1 = [preSum]  # 裡面放「左到右」的 preSum 答案，共有 1+n 種可能
        for i in range(n, 2*n):  # 「中間n個」逐一移動
            heappush(heap1, - nums[i])  # 左邊 max-heap（用負的）
            biggest = - heappop(heap1)  # 吐掉最大的（負的最小，就是最大）
            preSum = preSum + nums[i] - biggest  # 更新 preSum
            table1.append(preSum)  # 備份「全部的preSum」
        # 右邊的 n 個 ==================
        for i in range(3*n-1, 2*n-1, -1):  # 右邊的 postSum
            postSum += nums[i]  # 右邊 sum
            heappush(heap2, nums[i])  # 右邊 min-heap（用正的）
        # 右邊「每次都吐掉」最小的，便能留下「最大的n個」
        table2 = [postSum]  # 裡面將放「右到左」的 postSum，共有 1+n 種可能
        for i in range(2*n-1, 1*n-1, -1):  # 倒過來的迴圈，「中間n個」右到左「逐一移動
            heappush(heap2, nums[i])  # 右邊 min-heap
            smallest = heappop(heap2)  # 吐掉最小的
            postSum = postSum + nums[i] - smallest  # 更新 postSum
            table2.append(postSum)  # 備份「全部的postSum」
        table2 = table2[::-1]  # 反過來，便能改成「和table1一樣」左到右
        ans = [table1[i] - table2[i] for i in range(n+1)]  # 所有n+1種可能答案
        return min(ans)  # 找「最小值」
