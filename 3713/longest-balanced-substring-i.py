# LeetCode 3713. Longest Balanced Substring I
# 找出 s 的子字串，裡面字母出現次數一樣多。
class Solution:
    def longestBalanced(self, s: str) -> int:
        N = len(s)
        ans = 0  # 長度1000，可暴力2層迴圈
        for i in range(N):  # 子字串開始位置 i
            counter = Counter()  # 針對s[i]開始，統計字母
            for j in range(i,N):  # 結束位置 j
                c = s[j]  # 針對現在的字母 c
                counter[c] += 1  # 增加1次
                if j-i+1 < ans: continue  # 太短，不更新

                a = [v for v in counter.values()]
                for k in range(len(a)-1):  # 出現過字母的次數
                    if a[k]!=a[k+1]: break  # 不一致，跳掉
                else:  # 沒有 break 過，全部都一致，太好了!
                    ans = max(ans, j-i+1)  # 更新答案
        return ans
