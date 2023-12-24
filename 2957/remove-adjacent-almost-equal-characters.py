# 不希望字串裡「相鄰」的字母「相似」(相同 or 快要相同)
# 相同 'a'=='a' or 快要相同 'a'=='b'-1 或 'c'=='b'+1
# 問「要動幾個字母」才行。
class Solution:
    def removeAlmostEqualCharacters(self, word: str) -> int:
        N = len(word)
        s = list(word) # 轉成 list 方便修改
        def near(i,j): # 字母「相似」嗎？用ord()了解順序
            if ord(s[i])==ord(s[j]): return True
            if ord(s[i])==ord(s[j])-1: return True
            if ord(s[i])==ord(s[j])+1: return True
            return False
        ans = 0
        for i in range(1,N): # 巡 word[i-1] word[i] 
            # 只要有相鄰，就換吧，可以換離左右很遠的
            if near(i-1,i):
                s[i] = ' ' # 設到很遠的字母，不會與別人相似
                ans += 1
        return ans
        
