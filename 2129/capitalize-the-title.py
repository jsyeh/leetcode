# 將每個字的首字大寫
class Solution:
    def capitalizeTitle(self, title: str) -> str:
        words = title.split()  # 先斷字
        ans = []  # 用來放「首字大寫後」的每個字
        for word in words:  # 逐字分析
            if len(word)<=2:  # 題目說，短的字
                ans.append(word.lower()) # 都小寫
            else:  # 長的字
                ans.append(word.capitalize())  # 首字大寫
        return ' '.join(ans)
