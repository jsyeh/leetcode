# LeetCode 2429. Minimize XOR
# 兩數 num1 num2 請找 x （與num2有相同的0和1）使 x XOR num1 最小
class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        one1, one2 = 0, 0  # 數一下 num1 和 num2 有幾個 binary 1
        backup1, backup2 = num1, num2  # 備份 num1 num2，以進行剝皮、分析「有幾個1」
        while backup1 > 0 or backup2 > 0:  # 剝皮、分析「有幾個1」
            one1 += backup1 % 2  # 如果（現在）最低位是1，就+1
            one2 += backup2 % 2
            backup1 = backup1 // 2  # 剝皮後，就變小了
            backup2 = backup2 // 2
        # 了解有幾個1後，依照數量，有3種方法，決定怎麼放 1 到 x 裡
        if one1 == one2: 
            return num1  # 直接 num1 XOR num1 可全部「消掉」
        elif one1 < one2:  # 把「多的1」擺在「低位」
            # 如果 one2 比較多，那就把「多的1」擺在 x 的「低位」
            x = num1  # 要找的答案（先把 num1 全上，再把 0 補 1
            for bit in range(32):  # 「低到高bit」逐一開
                if one2-one1==0: break
                if x & (1<<bit) == 0:  # 可放bit
                    x |= (1<<bit)
                    one2 -= 1
            return x
        else:  # one1 > one2，就把 num1 的 1 從「高位到低位」消掉，可得到最小
            x = 0  # 要找的答案
            for bit in range(31,-1,-1):  # 倒過來的迴圈，位置高到低測bit
                if one2 == 0: break  # 用完 bit 1 就離開迴圈
                if 1<<bit & num1:
                    x |= (1<<bit)  # 把對應 bit 
                    one2 -= 1
            return x
