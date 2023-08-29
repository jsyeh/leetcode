# Y Yes, N No 從後到前數Y，從前到後數N
# 某格付出的代價=它之後的Y(包含)+它之前的N
class Solution:
    def bestClosingTime(self, customers: str) -> int:
        C = len(customers)
        Y = [0]*(C+1) # 右邊有幾個Yes(包含本身)
        N = [0]*(C+1) # 左邊有幾個No(不包含本身)

        for i in range(1,C+1): # 左邊開始數
            if customers[i-1]=="N": N[i] = N[i-1] + 1
            else: N[i] = N[i-1]
        
        for i in range(C-1, -1, -1): # 右邊有幾個Yes（包含本身）
            if customers[i]=="Y": Y[i] = Y[i+1] + 1
            else: Y[i] = Y[i+1]

        ans, min = 0, Y[0]
        for i in range(C+1):
            if Y[i] + N[i] < min:
                min = Y[i] + N[i]
                ans = i
        return ans
