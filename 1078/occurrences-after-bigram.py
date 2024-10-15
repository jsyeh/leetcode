# LeetCode 1078. Occurrences After Bigram
# Bi-gram 是二元組，如果 first 接 second 再接 third 的話，third是答案
class Solution:
    def findOcurrences(self, text: str, first: str, second: str) -> List[str]:
        text = text.split()  # 斷字
        ans = []
        for i in range(len(text)-2):  # 要退2格，因迴圈裡有 text[i+2]
            if text[i] == first and text[i+1] ==second:  # 符合條件
                ans.append(text[i+2])  # 就加答案
        return ans
