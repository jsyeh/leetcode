# 一開始在nums[0]。如果在nums[i]時，可往右1..nums[i]格，但不能超過範圍
# 問「最少要跳幾次」能跳到最後 nums[N-1]
# 總格子數有 10^4，不能使用O(N^2) 的演算法哦！
# 想到，可用「已走到的右邊界」來更新
class Solution:
    def jump(self, nums: List[int]) -> int:
        N = len(nums)
        step = defaultdict(int) # ex. step[3]「走3步」可達最右處
        nowStep = 0 # 一開始走0步
        step[0] = 0 # 第0步可走到0
        for i in range(N): # 目標是推動 step[nowStep] 右邊界
            if i>step[nowStep]: # 現在走到 nowStep後面的範圍
                nowStep += 1 # 需要多走1步了
            # 更新可以走到的範圍，往右推「可超過右邊界」
            step[nowStep+1] = max(step[nowStep+1], i+nums[i])
        return nowStep
