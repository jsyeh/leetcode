# LeetCode 2599. Make the Prefix Sum Non-negative
# nums 每次把1個數「移到最後面」，要做幾次，可讓它的 prefix sum 的陣列裡都沒有負
class Solution:
    def makePrefSumNonNegative(self, nums: List[int]) -> int:
        queue = deque(nums)  # 就照著模擬就好，使用 queue 剛剛好
        prefix = 0  # 一開始 prefix是 0
        ans = 0  # 要做幾次「移到最右邊」的動作呢？
        heap = []  # 重點：若需要時，要把「之前最小、負最多」的數，移動最後面
        while queue:
            now = queue.popleft()  # 排最前面的
            heappush(heap, now)  # 請過這個閘門，到「對面」
            prefix += now  # 現在「對面」的 prefix 更新一下
            if prefix < 0:  # 如果不幸「對面」過關的人「負能量太多」，失敗
                mostNegative = heappop(heap)  # 之前「負能量最多」的數，你！
                queue.append( mostNegative )  # 移到最後面（乖乖重新排隊）
                prefix -= mostNegative  # 現在少了那個傢伙，請重新評估一下
                ans += 1  # 要做一次「移到最後面」
        return ans
# 本來我笨笨的左出、右進，後來發現下面的測資，改用 heap 來把「負能量最多」的數，叫回去排隊
# test case 62/66: [6,-6,-3,3,1,5,-4,-3,-2,-3,4,-1,4,4,-2,6,0]
