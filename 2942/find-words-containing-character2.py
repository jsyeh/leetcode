# LeetCode 2942. Find Words Containing Character
# words 裡，有哪些字「含有x字母？」把對應的 index i 找出來
class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        ans = []
        for i in range(len(words)):  # 針對 words 裡的每個字
            if x in words[i]: ans.append(i)  # 若含有字母x，就加到答案裡
        return ans
