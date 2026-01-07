# LeetCode 1056. Confusing Number
# 數字倒過來時，還是可以看的數字，且值會不同（會看錯）
# 0,1,6,8,9 有潛力 confusing
class Solution:
    def confusingNumber(self, n: int) -> bool:
        counter = Counter(str(n))  # 先統計字母出現狀況
        for c in "23457":  # 只要有這些字母，就一定不行
            if counter[c]>0: return False  # 失敗

        # 用 table 對照表，將「數字倒過來」
        table = {'0':'0','1':'1','8':'8','6':'9','9':'6'}
        return list(str(n)) != [table[c] for c in reversed(str(n))]
