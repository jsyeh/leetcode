# LeetCode 2490. Circular Sentence
# 頭尾壓韻的意思：相鄰字的字母要相同，頭尾字（繞圈後）也相同。不相同，就失敗
class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        words = sentence.split()
        for i in range(len(words)-1):
            if words[i][-1]!=words[i+1][0]: return False  # 不相同，就失敗

        if sentence[0]!=sentence[-1]: return False  # 不相同，就失敗

        return True
