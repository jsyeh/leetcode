# 想看看 substrings 裡，有幾個「出現的數字頻率都相同」
# 字串長度<=1000
class Solution:
    def equalDigitFrequency(self, s: str) -> int:
        N = len(s)
        ans = set() # 算過、合格的答案
        for i in range(N):
            freq = defaultdict(int) # 字母目前出現次數
            most = 0 # 在字典裡出現最多的數
            for j in range(i,N):
                freq[s[j]] += 1 # 這個字母多出現一次
                most = max(most, freq[s[j]]) # 更新
                if most*len(freq)==j-i+1: # 乘起來等於長度
                    ans.add(s[i:j+1]) # 表示合格，加入
                
        return len(ans) # 有幾個答案
