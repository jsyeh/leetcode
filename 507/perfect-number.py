# perfect number: 把每個(可整除的)因數加起來, 剛好是自己
# 不過因為 num 有 10^8 超大的, 所以不能用暴力法
# 但可以用開根號, 來縮小迴圈的範圍
class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if num==1: return False # 因為不能包含N本身, 所以 1不合格
        total = 1 # 1一定是它的因數, 先計入
        for i in range(2, int(num**0.5)+1): # 迴圈從2開始, 避開1和N本身
            if num%i==0: 
                total += i # 把可整除的因數加起來
                print(i)
                if i != num//i: # 如果不重覆, 就把另一個對應的大的因數
                    total += num//i # 把可整除的因數加起來
                    print(num//i)
        if total == num: return True
        else: return False
# case 97/98: 1 特殊狀況, 因為不能包含N本身, 所以 1不合格
