# Y Yes, N No
# 想到：從後到前數Y，從前到後數N
# 某格付出的代價=它之後的Y(包含)+它之前的N
class Solution:
    def bestClosingTime(self, customers: str) -> int:
        N = len(customers)
        penaltyY = [0]*(N+1) # 右邊有幾個Y
        penaltyN = [0]*(N+1) # 左邊有幾個N
        for i in range(N): # 正順序看N
            if customers[i] == "N":
                penaltyN[i] = penaltyN[i-1] + 1
            else: # Y
                penaltyN[i] = penaltyN[i-1]
        for i in range(N-1,-1,-1): # 倒過來看Y
            if customers[i] == "Y":
                penaltyY[i] = penaltyY[i+1] + 1
            else:
                penaltyY[i] = penaltyY[i+1]
        ans, minPenalty = 0, penaltyY[0]
        for i in range(1,N+1):
            if penaltyY[i] + penaltyN[i-1] < minPenalty:
                ans = i
                minPenalty = penaltyY[i] + penaltyN[i-1]
        return ans
            
