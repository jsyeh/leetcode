# LeetCode 2462. Total Cost to Hire K Workers
# costs[i] 可聘用第i個人，每次從「最左 or 最右」candidates 的數量裡，挑「最便宜」的人，共挑k人
class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        N = len(costs)
        heap = [(costs[i], 0) for i in range(candidates)]  # 左邊
        heap += [(costs[-1-i], 1) for i in range(min(candidates,N-candidates))]  # 右邊
        heapify(heap)
        left, right = candidates, len(costs)-1-candidates
        ans = 0
        while k>0 and left <= right:
            c, d = heappop(heap)
            print(c)
            ans += c
            if d==0: 
                heappush(heap, (costs[left],0))
                left += 1
            else:
                heappush(heap, (costs[right],1))
                right -= 1
            k -= 1
        for i in range(k):
            c, d = heappop(heap)
            print(c)
            ans += c
        return ans
