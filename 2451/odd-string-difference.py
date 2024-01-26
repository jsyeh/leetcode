# words 裡每個字長度都相同，都可算出 different陣列
# different 裡會放 word[i+1]-word[i] 的值
# 找出different陣列「和別人不同」的那個字串
# 可把 different陣列「轉成字串」以便用字典來看是否重覆
class Solution:
    def oddString(self, words: List[str]) -> str:
        repeat = defaultdict(int) # 看different是否重覆
        original = defaultdict(str) # different對應的字
        for word in words:
            different = ''
            for i in range(len(word)-1): # +1 配 -1
                # 利用 ord() 找出字母對應的數字，減出對應的差
                nowDiff = ord(word[i+1]) - ord(word[i])
                different += str(nowDiff) + ' ' # 數字+空格
            repeat[different] += 1
            original[different] = word # 對應回「原本的字」
        # 統計完後，看誰落單
        for different in repeat:
            if repeat[different]==1: # 如果找到落單的值
                return original[different] # 對應原本的字
