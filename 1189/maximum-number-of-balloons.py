# balloon 能組合出來，就是一組氣球，問 text 能湊齊「幾組氣球」
class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        balloon = Counter('balloon')
        text = Counter(text)
        if 'b' not in text: return 0 # 少了最基礎的字母'b'
        ans = text['b'] # 用最基礎的字母'b'，先決定基礎的倍數
        for c in balloon: # 針對氣球的每個字母元素
            if c not in text: return 0 # 缺少字母、失敗
            # 有了字母，再查看字母的倍數，找倍數最小值
            ans = min(ans, text[c]//balloon[c])
        return ans
