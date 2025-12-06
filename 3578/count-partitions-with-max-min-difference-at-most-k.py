# LeetCode 3578. Count Partitions With Max-Min Difference at Most K
# 這題超難：將 nums 切成幾段，希望「每段」裡面的「最大 - 最小 <= k」，有幾種切法
# 用「毛毛蟲」的移動，配合更新 mono queue (maxq 及 minq) 確認範圍內的最大最小值，再用DP來解
class Solution:
    def countPartitions(self, nums: List[int], k: int) -> int:
        MOD = 10**9+7  # 答案太大，要取「餘數」
        N = len(nums)  # 陣列的大小
        table = [1] + [0] * (N+1)  # table[i+1] 對應到 nums[i]結尾的全部可能切法
        now = 1  # 從 table[tail]...table[head] 累積的可能切法，將塞入 table[head+1]
        ans = tail = 0  # 毛毛蟲的尾巴
        maxq, minq = deque(), deque()  # mono queue 裡面對應「大到小」「小到大」的 index i
        for head in range(N):  # 毛毛蟲的頭，往右持續吃 nums[head]
            while maxq and nums[maxq[-1]] < nums[head]:  # 需更新 mono queue
                maxq.pop()  # 更新 maxq 裡的 index 將不夠格的「吐掉」
            maxq.append(head)  # 再壓入目前的 head index 
            while minq and nums[minq[-1]] > nums[head]:  # 需更新 mono queue
                minq.pop()  # 更新 minq 裡的 index 將不夠格的「吐掉」
            minq.append(head)  # 再壓入目前的 head index 
            while nums[maxq[0]] - nums[minq[0]] > k:  # 毛毛蟲不合規格（最大-最大，差太多）
                now = (now - table[tail]) % MOD  # 舊的範圍不合，要吐掉最左邊（舊尾巴）的可能
                tail += 1  # 尾巴往右縮一格
                if maxq[0] < tail: maxq.popleft()  # 讓maxq內的index在毛毛蟲範圍內
                if minq[0] < tail: minq.popleft()
            table[head+1] = now  # now 是 table[tail]...table[head] 這段毛毛蟲裡，累積的可能切法
            now = (now + table[head+1]) % MOD  # 新的 now 對應 table[tail].... table[head+1]的全部可能
        return table[N]
