# 兩個句子 sentence1 sentence2 裡的字，是否都互通
# 所以要將 sentenceSimilar 做出對照表
# 不過會有「一對多」的狀況，所以使用 set 來包含「所有相同的字」
class Solution:
    def areSentencesSimilar(self, sentence1: List[str], sentence2: List[str], similarPairs: List[List[str]]) -> bool:
        N1, N2 = len(sentence1), len(sentence2)
        if N1!=N2: return False # 長度不同，糟！

        # 建立 similarPair 對照表
        similar = defaultdict(set)
        for s1, s2 in similarPairs:
            similar[s1].add(s2)
            similar[s2].add(s1)

        for i in range(N1):
            if sentence1[i] == sentence2[i]: continue # 很好，相同
            if sentence2[i] in similar[sentence1[i]]: continue  # 很好
            return False
        return True
# case 33/49: ["an","extraordinary","meal"]
# ["one","good","dinner"]
# [["great","good"],["extraordinary","good"],["well","good"],["wonderful","good"],["excellent","good"],["fine","good"],["nice","good"],["any","one"],["some","one"],["unique","one"],["the","one"],["an","one"],["single","one"],["a","one"],["truck","car"],["wagon","car"],["automobile","car"],["auto","car"],["vehicle","car"],["entertain","have"],["drink","have"],["eat","have"],["take","have"],["fruits","meal"],["brunch","meal"],["breakfast","meal"],["food","meal"],["dinner","meal"],["super","meal"],["lunch","meal"],["possess","own"],["keep","own"],["have","own"],["extremely","very"],["actually","very"],["really","very"],["super","very"]]
# 它的 meal 對應一堆，但我的舊程式，只留下一個。
