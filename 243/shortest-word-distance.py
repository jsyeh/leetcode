# 每個字，在 wordsDict 裡都有對應的 index
# 找出 word1 和 word2 對應的 index 差
# 但 case 21/27 ["a","a","b","b"] "a" "b" 有重覆的字
# 要換新的方法。看了 Editorial 的解法，原來 one pass即可
# 巡一輪時，遇到 word1 就記 i1，遇到 word2 就記 i2
# 再時時查看 abs(i1-i2)

class Solution:
    def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        i1, i2 = -1, -1 # 遇到 -1 還沒找到，還不能算距離
        ans = len(wordsDict) # 最遠的距離
        for i in range(len(wordsDict)):
            if wordsDict[i]==word1: i1 = i
            elif wordsDict[i]==word2: i2 = i
            
            if i1==-1 or i2==-1: continue # 若還沒收齊

            ans = min(ans, abs(i1-i2)) # 更新 ans
        return ans
        '''
        # 建出 index 字典，對應 word 在 wordsDict 的index
        index = {word:i for i,word in enumerate(wordsDict)}
        return abs(index[word1]-index[word2])
        '''
# case 21/27: ["a","a","b","b"] "a" "b"
# 如果有重覆的字出現，那只用「簡單的字典」無法查到2個以上的數
