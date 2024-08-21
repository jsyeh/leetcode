# LeetCode 664. Strange Printer
# 奇怪的印表機：一次印出一堆「相同的字母」，再換下個字母「蓋掉某範圍的字」
class Solution:
    def strangePrinter(self, s: str) -> int:
        # 先使用「函式呼叫函式」來解這題
        @cache
        def helper(left, right):  # 左邊界...右邊界，印表機要印幾次，才能完成
            if left>right: return 0  # 在簡化問題過程中，不合理的左右界，就不用看

            ans = 1 + helper(left+1, right)  # 最爛的答案：左1用「1次」，右邊「簡化的問題」
            for k in range(left+1, right+1):  # 若要要「打孔」的k，斷開左半、右半
                if s[left]==s[k]: # 印 s[left] 時，可印很多，若相同，就順便印到k，可省1次
                    now = helper(left,k-1) + helper(k+1,right)  # 左右兩段紙帶，省1格，再細問
                    ans = min(ans, now)  # 若更小，就更新
            return ans  # 這個 left...right 的最佳答案在這裡

        return helper(0,len(s)-1)  # 全部的答案
