# LeetCode 670. Maximum Swap 把num裡,任2字母最多交換1次,找最大的數
class Solution:
    def maximumSwap(self, num: int) -> int:
        ans = num  # 最簡單的答案,就是本身
        s = list(str(num))  # 因 Python 字串不能變動，所以再改成 list
        N = len(s)  # 轉成字串/list後的大小，也是迴圈的大小
        for i in range(N):  # 左手i、右手j
            for j in range(i+1, N):  # 左手i、右手j
                s[i], s[j] = s[j], s[i]  # 交換 i,j 兩位數
                ans = max(ans, int(''.join(s)))  # 看數字是否更大，更新
                s[i], s[j] = s[j], s[i]  # 再交換回來
        return ans
