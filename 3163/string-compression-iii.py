# LeetCode 3163. String Compression III
# 字串壓縮演算法：重覆的字母數量，放在字母前面（數量不能>9)
class Solution:
    def compressedString(self, word: str) -> str:
        ans = []  # 用來存放答案
        prevC, prevN = '', 0  # 目前重覆的字母不存在（小心'0'會被塞入）
        for c in word:  # 每個字母，逐個分析
            if c==prevC and prevN<9:  # 前與前個字母相同，且不超過 9 個，就可累加
                prevN += 1  # 有可能「累加到9個」 
            else:  # 如果無法再累加，就要輸出「數字、字母」的組合
                ans.append(str(prevN)+prevC)  # 前面字母
                prevC = c
                prevN = 1
        ans.append(str(prevN)+prevC)  # 塞最後一筆的答案
        return ''.join(ans[1:])  # 因最前面會有個'0'要去掉，只用 ans[1:]
