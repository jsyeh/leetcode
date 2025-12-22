# LeetCode 960. Delete Columns to Make Sorted III
# 刪一些 column，讓「每個字都是左小、右大」
class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        M, N = len(strs), len(strs[0])  # 字串數量、字串長度
        @cache
        def helper(k0, k):  # 現在要處理（比較）前一項 col k0 到「現在 col k」
            if k==N:  # 終止條件：處理到字串最右邊
                return 0  # 最右邊，什麼都沒有，不用刪任何東西
            # 有兩種可能：col k 「刪」或「不刪」
            ans1 = helper(k0, k+1) + 1  # 若「刪」col k 的話，答案 + 1 
            if k0 == -1:  # 特別的（更左邊的）哨兵，可「不刪」任何東西
                ans2 = helper(k, k+1)  # 通過檢查，可「不刪」，繼續右看 k+1 項
                return min(ans1, ans2)
            else:  # 逐項檢查「能不能」「不刪」
                for i in range(M):  # 逐項「左右」檢查，確認「左小、右大」
                    if strs[i][k0] > strs[i][k]:  # 不符合「左小、右大」
                        return ans1  # 只能用第11行「刪」的結果
            ans2 = helper(k, k+1)  # 通過檢查，可「不刪」，繼續右看 k+1 項
            return min(ans1, ans2)  # 挑「刪最少」的結果
        return helper(-1, 0)  # 從最左邊的 col 0  開始處理
