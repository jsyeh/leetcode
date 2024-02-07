# 依照字母出現的頻率，由多到少，把字母重組
class Solution:
    def frequencySort(self, s: str) -> str:
        counter = Counter(s) # 先統計「字母出現次數」

        # (字母出現次數,原字母) 逐一塞入 freq 裡，方便排序
        freq = [(counter[c],c) for c in counter]
        freq.sort(reverse=True) # 多的在左邊、少的在右邊
        ans = []
        for (f,c) in freq: # 頻率由多到少，逐個處理
            ans.append(c*f) # 把 f個字母c塞進ans
        return ''.join(ans) # 再接成字串
