# LeetCode 592. Fraction Addition and Subtraction
# 把「分子/分母」的分數，進行「加法、減法」。
# 只要找到分母的「最大公因數」，再把分子、分母用「最大公因數」約分即可。
# 但「字串斷字」變成 「數字」時，程式很複雜。看StefanPochmann的Solution，
# 發現 re.findall() 可用 Regular Expression 寫「數字」文法，快速找到答案
class Solution:
    def fractionAddition(self, expression: str) -> str:
        nums = re.findall('[+-]?\d+', expression)
        # 可將 "-1/2+1/2" 變成 ['-1', '2', '+1', '2']
        # RE文法中 [+-]? 代表「可有加號or減號，也可沒寫」
        # RE文法中 \d+ 代表「有很多數字」所以，只要符合這個，就找出來，變成 list
        A, B = 0, 1  # 加總算出來的答案，目前是 0 也就是 0/1
        for i in range(0, len(nums), 2): # 兩兩1組，取資料
            a, b = int(nums[i]), int(nums[i+1])
            A = A*b + a*B  # 通分時，分子交叉相乘，算出答案的分子部分
            B = B * b  # 通分時，分母相乘，算出答案的分母部分
            common = gcd(A,B)  # gcd最大公因數，是分子、分母共同的部分
            A //= common # 再約分
            B //= common # 再約分
        return str(A) + '/' + str(B)  # 把答案字串算出來

