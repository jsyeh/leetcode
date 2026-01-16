# LeetCode 2975. Maximum Square Area by Removing Fences From a Field
# 要從 hFences 抽掉一些、從 vFences 抽掉一些，剩下的剛好做出的正方形，最大面積多大？
class Solution:
    def maximizeSquareArea(self, m: int, n: int, hFences: List[int], vFences: List[int]) -> int:
        diff = set()  # Hint 1 2 建議補「頭尾」柵欄 [1,m] 和 [1,n] 再排列組合
        for a,b in combinations(hFences + [1,m], 2):  # 用排列組合，挑2個
            diff.add(abs(a-b))  # 將可能的距離，放入 diff
        ans = 0  # 上面 hFences 建橫向邊框、下面 vFences 建直向邊框
        for a,b in combinations(vFences + [1,n], 2):  # 用排列組合，挑2個
            if abs(a-b) in diff:  # 如果 a b 距離「有出現過」，便能組「正方形」
                ans = max(ans, abs(a-b))  # 就更新答案
        if ans==0: return -1  # 若找不到答案
        return ans * ans % (10**9+7)  # 找到答案，算出面積（數字很大，要取餘數）
