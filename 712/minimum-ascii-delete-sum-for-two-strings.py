# LeetCode 712. Minimum ASCII Delete Sum for Two Strings
# 想讓 s1 和 s2 變相同，需要刪掉的字母「ASCII加總最少」
class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        N1, N2 = len(s1), len(s2)
        @cache
        def helper(i,j):  # 利用「函式呼叫函式」找答案
            if i==N1 and j==N2: return 0  # 兩邊一起走完，很好！
            if i==N1:  # s1[i] 走完，剩 s2[j] 走到底（全刪）
                return sum( [ord(s2[k]) for k in range(j,N2)] )
            if j==N2:  # s2[j] 走完，剩 s1[i] 走到底（全刪）
                return sum( [ord(s1[k]) for k in range(i,N1)] )
                
            ans1 = ord(s1[i]) + helper(i+1,j)  # 刪掉 s1[i]
            ans2 = ord(s2[j]) + helper(i,j+1)  # 刪掉 s2[j]
            if s1[i]!=s2[j]:  # 不相同，只需將上面 ans1 ans2 取 min
                return min(ans1, ans2)  # 看誰的 cost 小，就用它
            return min(ans1, ans2, helper(i+1,j+1))  # 相同，多試一種可能
        return helper(0,0)  # 「函式呼叫函式」求解
