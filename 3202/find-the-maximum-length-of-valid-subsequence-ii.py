# LeetCode 3202. Find the Maximum Length of Valid Subsequence II
# nums 陣列挑選 subsequence 使得「相鄰兩數」%k 都相等
# ex. k是2時，「相鄰兩數」%k == target 的 target 可以是 0, 1 和昨天一樣
# ex. k是3時，「相鄰兩數」%k == target 的 target 可以是 0, 1, 2
# ex. k是10時 「相鄰兩數」%k == target 的 target 可以是 0, 1, ... 9
class Solution:
    def maximumLength(self, nums: List[int], k: int) -> int:
        bestAns = 0  # 最好的答案
        for target in range(k):  # 這些都是可能的 target，決定某個 target
            # 「相鄰兩數」subsequence (sub[i-1]+sub[i]) % k == target
            # 則 sub[i] 要找「前一項結尾」是 (target - sub[i] % k + k) % k
            ans = [0] * k  # ans[now] 對應 結尾是 now 的最長長度
            for now in nums:  # 現在開始，逐項「累積」 now 要配 prev 以便湊出 target
                prev = (target - now % k + k) % k  # 因相減可能變負數，故先 + k 再 %k
                ans[now % k] = ans[prev] + 1  # 前一項結尾是 prev 的長度 + 1 當現在的結尾
            bestAns = max(bestAns, max(ans))  # 最好的答案
        return bestAns
