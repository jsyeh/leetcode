# 給整數 num, 把它的 16進位表示字串秀出來
# 如果遇到負數，就用「2的補數」來呈現。
# 使用 hex(num) 可轉成16進位，但負數有點問題
# Discussion 裡，有人說 num += 2**32 即可
# 註：題目是有說「不能用build-in函式」不過隨便啦，能過就好
class Solution:
    def toHex(self, num: int) -> str:
        if num<0: ans = hex(num+2**32) # 負數，就加2**32
        else: ans = hex(num)
        # 因為前會會多 '0x' 字串，所以 return ans[2:] 避開
        return ans[2:]
