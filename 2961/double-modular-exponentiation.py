# variables[i] 有 a,b,c,m, good 代表 ((a^b%10)^c)%m == target
# a的b次方 的個位數，再 c次方 再取 % m 餘數
# 因數字 <=1000 好像沒很大，但 1000次方，也是很嚇人的
# 應該有什麼數學性質，可調整公式
# 看了 Solutions 裡 LakshayBrejwal_1_0 的解法，自己實作 pow函式，邊做邊mod
class Solution:
    def getGoodIndices(self, variables: List[List[int]], target: int) -> List[int]:
        def myPow(a, b, m): # a^b % m, 因為 b<=1000 可用 二分法，持續算出來
            ans = 1
            while b>0: # 只要指數還有值，就繼續拆
                if b%2 == 1: # 奇數
                    ans = (ans * a) % m # 只乘1個數
                # 就變偶數了
                a = (a * a) % m # 變成平方，也就是「折了b，翻倍a」
                b = b // 2 # 「折了b，翻倍a」
            return ans

        ans = []
        for i, var in enumerate(variables):
            # 因為用了兩次 a^b%m 的寫法，就照做
            part1 = myPow(var[0], var[1], 10)
            part2 = myPow(part1, var[2], var[3])
            if part2 == target: # 符合條件
                ans.append(i)
        return ans
