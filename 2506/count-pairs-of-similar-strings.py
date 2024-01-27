# words 裡的 word 有多少組「用到全部相同的字母」
# 可先算出每個 word 的 set() 再比較 set 是否相同
class Solution:
    def similarPairs(self, words: List[str]) -> int:
        sets = [set(word) for word in words] # 逐字變成 set()

        ans = 0
        for i in range(len(words)): # 左手i
            for j in range(i+1, len(words)): # 右手j
                if sets[i]==sets[j]: ans += 1 # 如果相同，答案+1
        return ans
