# LeetCode 726. Number of Atoms 字串 formula 化學分子式，有許多元素，問裡面元素各有幾個
# CO2, H2O, Mg(OH)2, K4(ON(SO3)2)2, Mg(H2O)N, (H) 等，組合規則很煩瑣，有字母、數字，重點是括號。
# 遇數字or大寫or括號，就斷字。括號對應stack，遇上括號：加Counter，遇下括號：吐Counter
class Solution:
    def countOfAtoms(self, formula: str) -> str:
        stack = [Counter()]
        self.num, self.now = 0, ''  # 利用 self 來取用 class 內的全域變數
        def processing(c):  # 為程式碼簡化，改成「函式」來處理
            if c.isupper() or c=='' or c=='(' or c==')': # 前段結尾/斷字，更新倍數
                if isinstance(self.now, str):  # now是字串，就更新對應num
                    stack[-1][self.now] += 1 if self.num==0 else self.num
                else:  # 「整坨now」 是 Counter(), 放大 num 倍
                    if self.num>0:  # 有倍數
                        for k in self.now:
                            self.now[k] *= self.num
                    stack[-1] += self.now  # 合併 counter
                self.num, self.now = 0, ''  # 新的開始
            if c.isdigit(): self.num = self.num * 10 + int(c)  # 遇到數字，更新倍數 （10 進位）
            elif c.isupper(): self.now = c  # 大寫，開始元素的名字
            elif c.islower(): self.now += c  # 小寫，接續元素的名字
            elif c=='(': stack.append(Counter())  # 上括號，加入「新Counter」
            elif c==')': self.now = stack.pop()  # 下括號，吐出 Counter，準備「整坨now」倍數成長
        for c in formula:  # 逐字母處理
            processing(c)  # 每個字母都做處理
        processing('')  # 字串結尾時，需要再最後處理（收尾、更新倍數）
        stack[0][''] = 0 # 空字串不秀出來，要清為0
        return ''.join(k+str(v if v>1 else '') for k,v in sorted(stack[0].items()))

