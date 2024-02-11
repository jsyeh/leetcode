# 將 words 變成 words[0]#words[1]# 之類的字串
# 想讓字串最短，也就是「能重覆用的postfix」就重覆用
# 那其實等價於「字串先反過來」再將字串排序，如果有 prefix 就省略它。
# 把 words 變少後，最後再 sum(len(word) for word in words) + len(words)
class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        words = [word[::-1] for word in words] # 將字串全部反過來
        words.sort() # 小到大排好
        # print(words)
        # 如果是 prefix 就省略它
        ansWords = []
        for i in range(len(words)-1):
            if not words[i+1].startswith(words[i]): # 不是 prefix
                ansWords.append(words[i]) # 就不能省略
        ansWords.append(words[-1]) # 最後1筆
        return sum(len(word) for word in ansWords) + len(ansWords)
