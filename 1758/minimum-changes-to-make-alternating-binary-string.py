# 11010101010
# 想把0101的字串「01交錯」問要換幾個bit
# 其實只有「兩種可能」，先0或先1，兩種都算一次，便知變最少的答案
class Solution:
    def minOperations(self, s: str) -> int:
        firstZero, firstOne = 0, 0 # 要變幾次，才能符合
        for i in range(len(s)):
            if i%2==0: # i從0開始嘛，所以是 first bit
                # 想知道不符合條件的有幾個（答案）
                if s[i]=='0': firstOne += 1 # 把0變1，才符合
                else: firstZero += 1 # 把1變0，才符合
            else: # 和上面的反過來
                if s[i]=='0': firstZero += 1# 把0變1，才符合
                else: firstOne += 1 # 把1變0，才符合
        return min(firstOne, firstZero)
