# LeetCode 2109. Adding Spaces to a String
# 要在字串裡，照著 spaces[i] 的位置，加入空格。
class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        words = []
        i0 = 0
        for i in spaces:  # 對著每一個空格的 index
            words.append(s[i0:i])  # 切割 i0...i 這段
            i0 = i  # 換下一個
        words.append(s[i0:])  # 最後一段
        return ' '.join(words)  # 再把字「串起來」
