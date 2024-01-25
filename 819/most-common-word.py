# 找出 paragraph 裡，沒有被 banned 的最常出現的字
class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        # 用 Regulation Expression 標示 splitter 有哪些字母
        words = re.split('[ !\?\',;.\"]', paragraph.lower() )
        print(words)
        freq = defaultdict(int)
        banned = {word for word in banned}
        for word in words:
            if word not in banned:
                freq[word] += 1
        ans = ''
        ansN = 0
        for word in freq:
            # 要避開空字串
            if word!='' and freq[word]>ansN:
                ans = word
                ansN = freq[word]
        print(freq)
        print(ansN)
        return ans
# case 5/48: "Bob. hIt, baLl" ["bob", "hit"]
