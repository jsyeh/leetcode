# LeetCode 2462. Total Cost to Hire K Workers
# costs[i] 可聘用「第i個人」，每次從「最左 or 最右」candidates 的數量裡，挑「最便宜」的人，共挑k人
class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        N = len(costs)  # 總共有 N 個人可以挑
        # print('N', N, 'k', k)
        ans = 0
        if candidates * 2 + k - 1 >= N:  # 能挑全部的人
            heapify(costs)  # 直接把 costs 陣列「變成heap」
            for i in range(k):  # 挑「最便宜」的k個人
                ans += heappop(costs)
        else:  # 左右慢慢挑
            heapLeft = costs[:candidates]  # 最左邊 candidates 個
            heapRight = costs[-candidates:]  # 最右邊 candidates 個
            left, right = candidates, N-1-candidates
            heapify(heapLeft)  # 變成 heap 資料結構
            heapify(heapRight)
            for i in range(k):  # 挑「最便宜」的k個人
                if heapLeft[0] <= heapRight[0]:  # 左邊最便宜
                    ans += heappop(heapLeft)
                    heappush(heapLeft, costs[left])
                    left += 1
                else:  # 右邊最便宜
                    ans += heappop(heapRight)
                    heappush(heapRight, costs[right])
                    right -= 1
        return ans
# Case 124/163: [28,35,21,13,21,72,35,52,74,92,25,65,77,1,73,32,43,68,8,100,84,80,14,88,42,53,98,69,64,40,60,23,99,83,5,21,76,34], 32, 12 
# 這個比較特別 N = 38，原本「分左右兩邊」但最後併在一起了。所以 改成 if candidates * 2 + k >= N:  # 能挑全部的人
# Case 162/163: [2,1,2], 1, 1
