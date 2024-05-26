# LeetCode 552. Student Attendance Record II
# 本題是延續 Easy 題 551. Student Attendance Record I
# 所以先解決 Easy 題的 for迴圈 + if 判斷，便有足夠的基礎，了解本題
# 接下來，使用「函式呼叫函式」的 Dynamic Programming 方法，從左到右依序處理
# 再改參數後，再呼叫同一個函式。記得要加 @cache 便可以有 memory功能，省下時間
# 但是不幸的，參數太多，當 n = 33943 之類的大數，memory會超過。 
# 觀察後，發現 'A' 只能有 0次 or 1次。
# 可先用類似 Fibonacci 數列的作法， a[i] = a[i-1] + a[i-2] + a[i-3] 做出數列
# 對應 'L' 連續遲到，在最後可接受0次、1次、2次 的 a.append(a[i]+a[i-1]+a[i-2])
# 完成整個數列後，再處理 1個 'A' 的缺課狀況：分成2半（左半、右半）的小問題，乘出可能數
# 最後再照題目要求，取 MOD 超大質數 10^9+7 的餘數。
class Solution:
    def checkRecord(self, n: int) -> int:
        if n==0: return 0  # 簡單的 case
        if n==1: return 3  # 只有1天，可對應 'P', 'L', 'A' 都行
        a = [1,1,2]  # 對應「只有'P'和'L'」的可能狀況（有幾種），但最後一項不是'L'
        MOD = 10**9+7  # 因為答案可能很大，所以題目照習慣，希望取 10^9+7 的餘數
        for i in range(2,n):  # 建出合理的表格，以便稍後查表
            a.append((a[i]+a[i-1]+a[i-2])%MOD)  # 有點像 Fiobonacci 數列的規則
            # 最後0個L、最後1個L、最後2個L，對應原數、少1數、少2數，以便放格子
        ans=(a[n]+a[n-1]+a[n-2])%MOD  # 只考慮 'P' 和 'L' 的可能性
        for i in range(n):  # 1個'A' 可能的位置 i:0...i:n-1
            ans=(ans+a[i+1]*a[n-i])%MOD  # 分成2半（左半、右半）的小問題，乘出可能數
        return ans
'''
class Solution:
    def checkRecord(self, n: int) -> int:
        MOD = 10**9 + 7
        @cache
        def helper(A, L, i):
            if i==n: return 1  # 走到最後1天
            # 如果這格正常出席 P，往下繼續
            ans = helper(A, 0, i+1)
            # 現在這格如果是缺席 A
            if A<1:  # 累積不到2天，可以缺席
                ans += helper(A+1, 0, i+1)  
            # 如果這格是遲到 L
            if L<2:  # 連續不到3天，可以遲到
                ans += helper(A, L+1, i+1)
            ans %= MOD  # 因為數字太大，只好 MOD (10^9＋7)
            return ans

        return helper(0,0,0)  # 第0天開始分析，累積0缺席、0遲到
'''
