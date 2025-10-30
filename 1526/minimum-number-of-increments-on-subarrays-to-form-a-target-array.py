# LeetCode 1526. Minimum Number of Increments on Subarrays to Form a Target Array
# 將原本都是0的陣列「每次挑一段 subarray 都+1」要做幾次，會與 target 完全相同
# 感覺跟「淹水」很像，看「剩下幾塊山頭」，但「暴力模擬」會很沒效率
# 但 coder206 畫出很棒的示意圖「只要知道累積提昇幾格」就是答案
class Solution:
    def minNumberOperations(self, target: List[int]) -> int:
        ans = target[0]  # 第0格的高度，需要「先做這麼多次」
        for i in range(len(target)-1):  # 接下來利用迴圈「兩兩比較」
            ans += max(0, target[i+1] - target[i])  # 看「提昇幾格」
        return ans
