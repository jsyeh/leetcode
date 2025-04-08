# LeetCode 3396. Minimum Number of Operations to Make Elements in Array Distinct
# 每次「刪掉前3個」，要幾次後，才能剩下的數「都不同」
class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        counter = Counter(nums)  # 利用 Counter() 統計數量
        bad = 0  # 有幾個「壞掉」的重覆的數
        for c in counter:
            if counter[c]>1: bad += 1  # 有「壞掉」的重覆
        removed = 0  # 開始進行操作「刪掉前3個」的對應 removed index
        while bad > 0:  # 只要還有重覆，就從頭開始「繼續刪」
            now = nums[removed]  # 現在要刪掉這個數
            counter[now] -= 1  # 出現次數 -1
            if counter[now]==1: bad -= 1  # 從「重覆」變「不重覆」，壞掉 -1
            removed += 1  # 又刪掉1個數了，index 往右移
        return (removed+2) // 3  # 神奇的公式，換算「需刪掉3個」幾次
