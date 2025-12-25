# LeetCode 3075. Maximize Happiness of Selected Children
# 挑選快樂的小朋友，被選到很開心，但還沒被選到的小朋友就漸漸不開心
# happiness[i] 都會減1，到0為止。要挑 k 位，得最高的「快樂分數」
class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        # 如果要挑的人比較少，不用 sort 而改用 priority queue 會更快。
        heap = [ - hap for hap in happiness ]  # 因 heap 先取小，所以加負號
        heapify(heap)
        ans = 0
        for i in range(k):
            now = - heappop(heap)  # 因 heap 先取小，所以加負號
            if now - i <= 0:  # 現在扣掉「漸漸不開心」後，若扣超過
                break  # 要能提早離開迴圈
            ans += now - i
        return ans
