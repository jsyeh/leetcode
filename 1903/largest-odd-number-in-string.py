# 要找到字串裡「最大的奇數」, 也就是那個子字串的結尾是 1,3,5,7,9 其中一個
# 因為「字串越長」對應的數字越大, 所以其實就是找「最長的奇數」
# 只要「從右到左巡」找到任一個奇數在 index i, 便能回傳 num[:i+1]
# 或是「從左到右巡」把每個奇數 index i 都更新 ansI, 便能回傳 num[:ansI]
class Solution:
    def largestOddNumber(self, num: str) -> str:
        # N = len(num) # 本來我猜這行要巡過一次,會比較慢, 所以用下一個方法
        for i in range(len(num)-1, -1, -1):
            if int(num[i])%2==1: return num[:i+1]
        return ""

        # 但沒想到上面那個好像比較快
        # i, ansI = 0, 0 # 很像 for 迴圈的 i
        # for c in num: # 因為不想要 len(num)巡一次, 所以改用這個迴圈
        #     i += 1 # 這其實是現在 index 的右一格, 這樣答案就不用寫 num[:ansI-1]
        #     if int(c)%2 == 1: ansI = i # 這個位數是奇數的話, 更新答案
        # return num[:ansI] # 最後的答案的字串, 從頭開始、最長的那個
