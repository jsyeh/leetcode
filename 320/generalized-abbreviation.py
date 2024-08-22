# LeetCode 320. Generalized Abbreviation
# 可把字母「用數字」來取代，像 Internationalization 縮寫成 i18n
# 但「數字不能相鄰」。請列出全部可能的縮寫
class Solution:
    def generateAbbreviations(self, word: str) -> List[str]:
        ans = [word]
        N = len(word)
        # 每一層呼叫，要間隔一個英文字
        for i in range(N): # 左邊界（包含）
            for j in range(i,N): # 右邊界（包含）
                # ...i..j...
                # ...[  ]x.. 其中 x 表示「要留下英文」才能再 rest 函式呼叫函式
                for rest in self.generateAbbreviations(word[j+2:]):
                    now = word[:i] + str(j-i+1) + word[j+1:j+2] + rest
                    ans += [now]
        return ans
