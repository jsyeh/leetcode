# A..Z 被編碼成 1..26, 所以 11 可能會變成 K 或 AA
# 要列出某個字串「所有編碼可能的個數」
# 使用「函式呼叫函式」
class Solution:
    @cache
    def numDecodings(self, s: str) -> int:
        if len(s)==0: return 1 # 成功收尾的1種可能
        if s[0]=='0': return 0 # 不合理,0種可能

        if len(s)==1: return 1 # 去除不合理的0, 現在一定也是1種可能

        if s[0]=='1':
            return self.numDecodings(s[1:]) + self.numDecodings(s[2:])
            # 左邊是拆1位 得1, 右邊是拆2位 得1x
        elif s[0]=='2' and s[1]<='6': # 這也在範圍內
            return self.numDecodings(s[1:]) + self.numDecodings(s[2:])
            # 左邊是拆1位 得2, 右邊是拆2位 得2x
        else: 
            return self.numDecodings(s[1:]) # 只能拆1位, 繼續解碼
        
# case 23/269: "111111111111111111111111111111111111111111111"
# 可能需要 @cache 讓重覆的部分不用重算
