# LeetCode 3714. Longest Balanced Substring II
# s 字串裡，只有3種字母 'a' 'b' 'c' 要找到最長的子字串，裡面「每種字母出現次數相同」
class Solution:
    def longestBalanced(self, s: str) -> int:
        preSum = [ (0,0,0) ] # 先統計3種字母的prefix sum出現累積數量，初始值「3種都是0」
        count = Counter()  # 3種字母的「累積數量」
        for c in s:  # 針對字串的字母逐一處理
            count[c] += 1  # 這種字母多1個
            preSum.append( (count['a'], count['b'], count['c']) )  # 統計累積數量
        ans = 1  # 若字串只有1個字母，一定符合條件
        prev = {}  # 存「3種字母的次數差」，若「再度出現」，「兩處中間」符合條件
        for i, (a,b,c) in enumerate(preSum):  # 每格的字母累積數量。下面參考 Alex Wice 的技巧，簡化「大量判斷」
            # 依序處理 「3字母都有」   「只有ab扣c」 「只有bc扣a」 「只有ac扣b」「只有a扣bc」「只有b扣ac」「只有c扣ab」
            for k in ('abc',a-b,b-c),('ab',a-b,c),('bc',b-c,a),('ac',a-c,b),('a',b,c),('b',a,c),('c',a,b):
                if k in prev:  # 字母的數字差「六種可能的其中一種」有正確的「再度出現」，「兩處中間」符合條件
                    ans = max(ans, i - prev[k])  # 更新答案的長度
                else:  # 沒出現過
                    prev[k] = i  # 就記錄出現的位置，等「後面」來「碰撞」
        return ans
