# beauty值是：字串裡「最多次數」-「最小次數」
# 這題要將「全部substrings」的beauty值加總
# 因為 500 個字母很短，決定先「暴力法」試試
class Solution:
    def beautySum(self, s: str) -> int:
        ans = 0
        counter = [Counter()]  # 要使用一堆 Counter() 來算答案
        for i in range(len(s)):  # 先建出右邊新的 counter[i+1]
            counter.append(Counter(s[i]) + counter[-1])
            for k in range(i):  # 再減掉左邊舊的 counter[k]
                diff = counter[i+1] - counter[k]
                ans += max(diff.values()) - min(diff.values())  # beauty值
        return ans
