# 題目找出「字慢慢增加」的chain，每次只能加1個字母
# 字的長度最長是16字母，總共有1000個字
class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        words.sort(key=lambda x : len(x)) # 照字母長度排序
        table = {} # table["bdca"] 可查出 longest chain 組出 "bdca"

        ans = 1 # 
        for w in words:
            table[w] = 1
            for i in range(len(w)): # 每次挑個字母消失
                shorter = w[:i] + w[i+1:] # 刪第i個字母後 shorter
                if shorter in table: # 如果這個短一點的字，有在資料庫裡
                    table[w] = max(table[w], table[shorter]+1) 
                    # 用它更新table[w]
                    if table[w]>ans: # 若 StrChain更長，更新答案
                        ans = table[w]
            
        return ans
