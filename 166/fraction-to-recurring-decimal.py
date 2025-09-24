# LeetCode 166. Fraction to Recurring Decimal
# 分子/分母，得到小數部分。如果有「循環小數」時，用圓括號括起來。 ex. 4/3 得到 1.(3)
class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        part1 = numerator // denominator  # Part1 「整數部分」
        mod = numerator % denominator  # 先得到「餘數」
        if mod==0:  # 可以「整除」（餘數為0）便提早結束
            return str(part1)  # 只有「整數部分」，可提早結束
        if part1 < 0:  # 遇到負的，怎麼辦？分類處理
            part1 += 1  # 先補1
            if part1 == 0: part1 = '-0'
            mod = denominator - mod
        table = {}  # 對照表，檢查「重覆出現」的「餘數」在哪裡
        part2 = []  # 小數點以下「每個位數」
        for i in range(10000):  # 題目保證 10^4 長度之前會循環，所以迴圈跑這麼多次
            if mod==0:  # 可以「整除」（餘數為0）便提早結束
                return str(part1) + '.' + ''.join(part2)  # 整數、小數點、小數
            if mod in table:  # 找到「循環小數」開始重覆
                start = table[mod]  # 「循環小數」開始重覆的「位置」
                break
            table[mod] = i  # 記錄「曾經出現」的「餘數」的「位置」
            part2.append( str(mod * 10 // denominator) )  # 殘留在「這個位數」的數字
            mod = mod * 10 % denominator  # 算出新的「餘數」
        part2.insert(start, '(')  # 「循環小數」開始重覆 插入開始「位置」的「圓括號」
        part2.append(')')  # 最後收尾的「圓括號」
        return str(part1) + '.' + ''.join(part2)  # 整數、小數點、小數（含圓括號）
