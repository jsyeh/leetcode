# LeetCode 1106. Parsing A Boolean Expression
# 字串 expression 裡有 True,False,NOT,AND,OR，分析parse出運算結果。在分析語法，可使用 Stack 來放資料
class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        val = []  # Value Stack 放 True, False 的值
        op = []  # OP Stack 放 NOT,AND,OR 的運算指令
        for c in expression:  # 針對字串「逐字母」分析
            if c=='!' or c=='&' or c=='|': op.append(c)  # 塞入「運算符號」
            elif c=='t':  # 值 True
                ans = True  # 隨時更新 ans
                val.append(True)
            elif c=='f':  # 值 False
                ans = False  # 隨時更新 ans
                val.append(False)  # 塞入「值」
            elif c=='(': val.append('(')  # 「上括號」後面會「接」一堆數值
            elif c==')':  # 最難在這裡：要照 op 運算，處理 val
                nowOp = op.pop()
                if nowOp=='!':  # NOT 運算
                    ans = not val.pop()
                    val.pop()  # 把「上括號」吐掉
                    val.append(ans)
                elif nowOp=='&':  # AND 運算
                    ans = True  # AND 的基礎是 True
                    while True:
                        now = val.pop()  # 逐個往回吐
                        if now=='(': break  # 往回遇到「上括號」就停
                        ans &= now
                    val.append(ans)
                elif nowOp=='|':  # OR 運算
                    ans = False  # OR 的基礎是 False
                    while True:
                        now = val.pop()  # 逐個往回吐
                        if now=='(': break  # 往回遇到「上括號」就停
                        ans |= now
                    val.append(ans)
        return ans  # 最後更新、殘留的 ans 是最後的答案
