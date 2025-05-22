# LeetCode 3362. Zero Array Transformation III
# queries 裡 [left, right] 可將 nums[left]...nums[right] 挑些數「減1」
# 希望 nums 能全部變成 0，而 queries 有些其實「刪掉不用」也能達成任務：最多可「刪掉幾個？」
# 策略：先把 queries 排序，再用 heap 逐一判斷 nums[i]「是否能用」「是否需要」某個 queries 幫忙
class Solution:
    def maxRemoval(self, nums: List[int], queries: List[List[int]]) -> int:
        queries.sort(reverse=True)  # Hint 1 排序（將用 pop()取出，所以「反過來」小的在右邊）
        # Hint 2 先挑 query 「結束時間較遠的」因「包含的範圍較大」，所以使用 2 個 heap
        heapAvailable = []  # 目前「範圍有效」「能用的 query」。小心！結束時間晚的優先（heapAvailable加負號）
        heapUsing = []  # 「正在使用」的 query，在 heap 記錄它的「結束時間」（過期的會失效）
        for i in range(len(nums)):  # 依序處理 nums[i]
            while queries and queries[-1][0] <= i:  # 把「開始」在 i 之前「能用的 query」
                left, right = queries.pop()  # 都取出，放入 heapAvailable 裡
                heappush(heapAvailable, -right)  # 記下結束時間。「結束時間」越後面越好（heapAvailable加負號）
            while heapUsing and heapUsing[0] < i:  # 把「結束時間」在 i 之前將失效的 query
                heappop(heapUsing)  # 就丟掉（過期的會失效）
            while nums[i] > len(heapUsing):  # 正在使用的 query，若數量不夠
                if len(heapAvailable)==0: return -1  # 沒有「能用的 query」，失敗
                if i > - heapAvailable[0]: return -1  # 時間接不上（結束時間沒能含i），失敗（heapAvailable加負號）
                biggestEnding = - heappop(heapAvailable)  # 挑「最遠才結束」來用（heapAvailable加負號）
                heappush(heapUsing, biggestEnding)  # 拿來用
        return len(heapAvailable)  # 還沒用的、還剩下來的、可節省下來的 query
