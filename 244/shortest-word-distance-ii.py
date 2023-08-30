# 在wordsDict字典裡，有些字出現不只一次。所以不能只存i,要存 sorted list
# 剛好是用 for迴圈逐個 append(i) 所以保證已排序
class WordDistance:

    def __init__(self, wordsDict: List[str]):
        # print("wordDict", wordsDict)
        self.table = {}
        for i, word in enumerate(wordsDict):
            if word in self.table:
                self.table[word].append(i) # 保證小到大排好
            else:
                self.table[word] = [i]

    def shortest(self, word1: str, word2: str) -> int:
        list1 = self.table[word1]
        list2 = self.table[word2]

        i1, i2 = 0, 0
        min_diff = inf
        while i1 < len(list1) and i2 < len(list2):
            min_diff = min(min_diff, abs(list1[i1]-list2[i2]))
            if list1[i1] < list2[i2]:
                i1 += 1 # 比較小的，就努力趕上、想拉近距離
            else:
                i2 += 1 # 比較小的，就努力趕上、想拉近距離

        return min_diff

# Your WordDistance object will be instantiated and called as such:
# obj = WordDistance(wordsDict)
# param_1 = obj.shortest(word1,word2)
