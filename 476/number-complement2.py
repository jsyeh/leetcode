# LeetCode 476. Number Complement 計算機概論「二進位」的補數（0變1、1變0）
# 另外一種方法，是可以轉成2進位的字串，再逐位處理
# 但怎麼把數字，變成 binary 形狀的字串呢？ google: python int binary 找到
# https://stackoverflow.com/questions/699866/convert-int-to-binary-string-in-python
# 方法1: '{0:b}'.format(num) 方法2: bin(num) 方法3: f'{num:b}'
class Solution:
    def findComplement(self, num: int) -> int:
        # 因字串「沒辦法修改內容」，要用 list() 把「字串」變成 list，使能修改。
        num = list(bin(num)[2:])  # 因為 bin(5) 會變成 '0b101' 要去掉左邊2個字母 [2:]
        for i in range(len(num)):  # 「左到右」逐個處理
            if num[i]=='0': num[i] = '1'  # 把 num[i] 從 '0' 變成 '1'
            else: num[i] = '0'  # 把 num[i] 從 '1' 變成 '0'
        return int(''.join(num), 2)  # 先把 list 用 ''.join() 接成字串，再變成「2進位整數」

