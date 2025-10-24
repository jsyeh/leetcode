# LeetCode 2048. Next Greater Numerically Balanced Number
# 找到 n 以上的數，剛好出現的位數，剛好與次數相同。ex. 22 對應 2 出現2次，很好
# ex. 1333 對應 1 出現1次， 3 出現3次，很好。
class Solution:
    def nextBeautifulNumber(self, n: int) -> int:
        # 這題的測資較小，只有 10^6，可能可以「暴力去試」
        for i in range(n+1, n*100+2):  # 我猜：試100倍，應該可以成功吧！
        # 但有筆測資是 n=0 再乘100倍也沒有，所以隨手加個2，好像就好了
            counter = Counter(str(i))  # 變成字串，再計數
            bad = False  # 檢測之前「沒壞」
            for d in counter:  # 逐位數檢查
                if int(d) != counter[d]: bad = True  # 數量不符合，失敗
            if not bad: return i  # 沒失敗，就是找到答案，很好！
