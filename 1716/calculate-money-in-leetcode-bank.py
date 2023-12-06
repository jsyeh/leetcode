class Solution:
    def totalMoney(self, n: int) -> int:
        table = [1,2,3,4,5,6,7] # 前7天的基礎存的錢
        if n<7: return sum(table[:n]) # 少於7天的話，就部分加起來

        for i in range(7,n): # 很多天的話，就逐一加吧！
            table.append(table[i-7]+1) # 比7天前，多1元
        # print(table) # 檢查一下，果然正確
        return sum(table) # 開心加總起來
