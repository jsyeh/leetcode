# LeetCode 3396. Minimum Number of Operations to Make Elements in Array Distinct
# 每次「刪掉前3個」，要幾次後，才能剩下的數「都不同」
class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        table = [0] * 101  # 對照表，標示 1...100 的數「出現過幾次」
        N = len(nums)  # 總共有 N 個數
        good = 0  # 從尾巴開始數，有幾個 good 的數（不會造成「重覆」）
        for i in range(N-1, -1, -1):  # 倒過來的迴圈
            table[nums[i]] += 1  # 現在這個數的數量 + 1
            if table[nums[i]] == 2: break  # 若有重覆，就壞掉，離開
            good += 1  # 沒有重覆，很好 good +1
        return (N-good+2) // 3  # 神奇的公式，換算「刪掉前3個」要做幾次
