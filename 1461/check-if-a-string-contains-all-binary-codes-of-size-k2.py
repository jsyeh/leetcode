# LeetCode 1461. Check If a String Contains All Binary Codes of Size K
# 長度為 k 的全部二進位字串(ex. 00 01 10 11) 是否全在字串s裡出現
class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        happened = set()  # 「出現過」的小字串
        for i in range(len(s)-k+1):  # 先逐一收集「小字串」
            happened.add(s[i:i+k])  # 將長度 k 的小字串加入集合
        return len(happened) == 2**k  # 看是否「收齊全部的小字串」
        
# 第6行 for i in range(len(s)-k+1) 如果漏寫 +1，下面的測資會出錯
# case: 186/201: "00110" k=2
