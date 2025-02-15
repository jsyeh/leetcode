# LeetCode 2698. Find the Punishment Number of an Integer
# 有一種神奇的「懲罰數」，像 1 (1*1得到1)，81（9*9得81，切8+1剛好是9）
# 100（10*10得100，切10+0剛好是10），1296（36*36得1296，切1+29+6剛好是36）
# 找出一堆 i <= n，將 i*i 是懲罰數的都「加起來」。可用「函式呼叫函式」把所有的可能「暴力」切看看
class Solution:
    def punishmentNumber(self, n: int) -> int:
        @cache
        def helper(s, target):  # 字串 s 切出一些數，剛好「加起來」是target
            if int(s) == target: return True  # 剛好字串「本身」的值就是 target，成功
            if s=='' and target!=0: return False  # 剛好都切完時，但 target 不對，失敗
            if target<=0: return False  # 切到 target 變負的，也是失敗
            for i in range(1,len(s)):  # 用迴圈，把所有的可能「暴力」切看看
                if helper(s[i:], target-int(s[:i])):  # 只要有其中一種切法成功
                    return True  # 就成功
            return False  # 都沒成功，就失敗
        ans = 0
        for i in range(1,n+1):
            if helper(str(i*i), i): 
                ans += i*i
        return ans
