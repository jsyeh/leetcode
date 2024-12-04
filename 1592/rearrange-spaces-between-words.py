# LeetCode 1592. Rearrange Spaces Between Words
# 重新調整「字與字之間」的「空格數量」
class Solution:
    def reorderSpaces(self, text: str) -> str:
        N = len(text)  # 總長度
        S = text.count(' ')  # 空格的數量
        words = text.split()  # 斷字
        S2 = len(words)-1  # 有幾個間格
        # 小心，如果只有1個字，就全部補在最後
        if S2==0: return words[0]+' '*S 

        S3 = S // S2  # 「最後」字間的空格數
        ans = (' '*S3).join(words)  # 插好「字間的空格」
        ans += ' '*(S % S2)  # 補齊「最後的空格」
        return ans
