# 11010101010
# 想把0101的字串「01交錯」問要換幾個bit
# 其實只有「兩種可能」，先0或先1，兩種都算一次，便知變最少的答案
# 我原本的寫法的邏輯看起來比較複雜，所以我又換了另一種寫法
# 比較慢，但是把兩種狀況，用兩個迴圈分開思考，比較好懂
class Solution:
    def minOperations(self, s: str) -> int:
        evenOne = 0 # 希望i%2==0偶數位是1、i%2==1奇數位是0
        # 希望是 10101010
        for i in range(len(s)): # 但不合理時，如下變動
            if i%2==0 and s[i]=='0': evenOne += 1
            if i%2==1 and s[i]=='1': evenOne += 1

        oddOne = 0 # 希望i%2==1奇數位是1, i%2==0偶數位是0
        # 希望是 01010101
        for i in range(len(s)): # 但不合理時，如下變動
            if i%2==1 and s[i]=='0': oddOne += 1
            if i%2==0 and s[i]=='1': oddOne += 1

        return min(evenOne, oddOne)
