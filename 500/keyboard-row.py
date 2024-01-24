# 上 "qewrtyuiop" 中 "asdfghjkl" 下 "zxcvbnm"
# 問 words 裡，哪些字是「集中在同一row」
class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        row = [ set("qwertyuiop"), set("asdfghjkl"), set("zxcvbnm") ]
        ans = []
        for word in words:
            word2 = word.lower()
            count = [0]*3
            for c in word2:
                for i in range(3):
                    if c in row[i]: count[i] += 1
            wordLen = len(word)
            if count[0]==wordLen or count[1]==wordLen or count[2]==wordLen:
                ans.append(word) # 加入答案
        return ans
