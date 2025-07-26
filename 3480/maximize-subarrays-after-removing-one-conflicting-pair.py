# LeetCode 3480. Maximize Subarrays After Removing One Conflicting Pair
# 1...n 陣列中，conflictingPairs[i] = (a,b) 代表 a b 衝突、不能在一起
# 將「1組限制」刪掉，最多有幾種 subarray 不含「剩下的 conflictingPairs」？ 
# 照著 awice 的解題策略：「全部限制都在」+「（刪掉某一組限制）額外賺到的值」
class Solution:
    def maxSubarrays(self, n: int, conflictingPairs: List[List[int]]) -> int:
        # right[i] 對應：每個數 i 若當右界時，左邊有哪些可能的起點
        right = [[] for i in range(n+1)]
        for a, b in conflictingPairs:  # 每組「衝突pair」都會將「subarray」斷開
            R, L = max(a,b), min(a,b)  # （最大值）右界 R 對應的（最小值）左界 L
            right[R].append(L)  # 將「全部的衝突限制」以「右界R有個左界L」逐一記錄
        ans = 0  # 「全部限制都在」的「基礎答案」
        left = [0, 0]  # left[0] 是最大的左界，left[1] 是第二大的左界（會持續更新）
        improve = [0 for i in range(n+1)]  # improve[i]：若限制(i..R)刪掉, 能改善的幅度
        for R in range(1,n+1):  # 1..n之間，左到右「逐一」決定 R 右界。想像拉個捲尺，從右r往左拉，有幾種可能
            for L in right[R]:  # 右界 R 對應的「左界L的全部可能」逐一測試「會卡住的地方」
                left = max(left, [left[0], L], [L, left[0]])
                # left[0], left[1], L 這3個數，把最大的放 left[0] 第二大的放 left[1]
                # 可想像成 L 有 3 個地方可以放： left[0],left[1],L vs. left[0],L,left[1] vs. L,left[0],left[1]
                #                            ^^^^^^^^^^^^^^^       ^^^^^^^^^             ^^^^^^^^^
            improve[left[0]] += left[0] - left[1]  # 若唯一刪掉「限制條件」是 (left[0], R) 
            # left[1]..left[0]..R 可增加的量 是 left[1]...left[0] 這段。迴圈在其他 R 也會增加這段，故把它加到 left[0] 對應邊界
            ans += R - left[0]  # 若刪掉 (left[0], R) 額外賺到的值
        return ans + max(improve)  # 答案：「全部限制都在」+「（刪掉某一組限制）額外賺到的值」
