# 這題很簡單，問「字母」移來移去後，能不能「平均分配」讓word相同
# 只要先逐一統計「字母」出現的字數，再檢查「是否是N的倍數」即可
class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        N = len(words) # 最後要平分給N個word哦！
        H = defaultdict(int) # 統計字母 H[c] 出現次數
        for word in words: # 逐字統計
            for c in word: # 逐字母統計
                H[c] += 1 # 增加1個字母，很好
        # 下面在 H 裡逐個檢查，是否都是N的倍數
        for c in H:
            if H[c]%N != 0: return False # 不是，就失敗
        return True # 檢查通過,就成功
