# LeetCode 476. Number Complement 計算機概論「二進位」的補數（0變1、1變0）
# 另外一種方法，是可以轉成2進位的字串，再逐位處理
# 但怎麼把數字，變成 binary 形狀的字串呢？ google: python int binary 找到
# https://stackoverflow.com/questions/699866/convert-int-to-binary-string-in-python
# 方法1: '{0:b}'.format(num) 方法2: bin(num) 方法3: f'{num:b}'
class Solution:
    def findComplement(self, num: int) -> int:
        num = f'{num:b}'  # 用 2進位的方式，把 num 變成 '101' 之類的字串
        ans = '' # 空空的字串，利用「字串加法」把答案「逐一」加進來
        for c in num:  # 「左到右」逐個處理
            if c=='0': ans += '1'  # 答案多個字母 '1'
            else: ans += '0'  # 答案多個字母 '0'
        return int(ans, 2)  # 把「2進位字串」字串，轉換成「整數」
