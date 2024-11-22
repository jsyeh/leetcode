# LeetCode 1072. Flip Columns For Maximum Number of Equal Rows
# matrix 可 col flip （直行 0/1 交換），希望 rows 橫條一樣都一樣的值
# 本來我沒有頭緒，參考 Lee215 解法下方 am1 留言的程式，突然就懂了！
# flip 就是「0變1」或「1變0」，直行flip就對應「每個row的特定bit」一起變化
# 所以，某兩個row「長得一樣」就可「一起變成全0或全1」。用 Hash Map 統計row的形狀即可
class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        counter = Counter()  # 用 Hash Map 計數器，記錄「row的形狀」相同有幾個
        for row in matrix:  # 把每個row「逐一統計」
            if row[0]==1:  # 統一讓 row 開頭都是0，故「遇到1」就要全反
                row = [1-c for c in row]
            # 統計row的形狀
            counter[tuple(row)] += 1  # 轉成 tuple 才能加入 Hash Map
        return max(counter.values())  # 找出「出現次數最多」的次數
