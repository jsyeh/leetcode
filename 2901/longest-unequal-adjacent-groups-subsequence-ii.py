# LeetCode 2901. Longest Unequal Adjacent Groups Subsequence II
# 找最長 subsequence 裡面「相鄰的項」groups不相同、words[i] words[j]長度相同、只差1字母
class Solution:
    def getWordsInLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        n = len(words)  # words 有幾個數
        prev = [-1] * n  # 用來「指到」前一項，也就是 words[i] 前一項是 prev[i]
        @cache  # 利用 cache 加速
        def hammingOne(i, j):  # 判斷2字串的距離「剛好是1」的狀況
            if len(words[i]) != len(words[j]): return False  # 長度不同，失敗
            diff = 0  # 兩字串的距離
            for k in range(len(words[i])):  # 逐字母比較
                if words[i][k] != words[j][k]: diff += 1  # 不同的字母有幾個
            return diff==1  # 剛好「距離是1」
        @cache  # 可用 DP 「函式呼叫函式」解這題
        def helper(k):  # 「使用words[k]結尾」的最長 subsequence
            if k==0: return 1  # 最基礎的 case 就 words[0] 這1個字
            ans = 1  # 最長的長度，至少有 words[k] 本身1個
            for i in range(k):  # 查看前幾項，看能不能「接起來」
                now = helper(i)
                if groups[i] != groups[k] and hammingOne(i,k) and now + 1 > ans:
                    ans = now + 1  # words[k] 可經由 words[i]「接起來」，而且是更長的接法
                    prev[k] = i  # 前一項便是 i
            return ans
        longest = 0  # 想找「最長」的接法
        for i in range(n):
            now = helper(i)
            if now > longest:  # 若長度更長
                longest = now  # 更新
                end = i  # 最適當的結束位置
        ans = [end]  # 利用「回溯法」，從「最適當的結束位置」往前回溯
        while prev[ans[-1]] != -1:  # 一直回溯，直到「無法再回溯」為止
            ans.append(prev[ans[-1]])  # 依序將 index i 加入 聞
        return [words[i] for i in reversed(ans)]  # 再「倒過來」找到對應的 words[i]
