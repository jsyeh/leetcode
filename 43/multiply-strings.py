class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        # Python 的話，直接用 eval() 好像輕鬆很多，但花了39ms
        # return str(eval(num1+"*"+num2))
		# 下面逐一模擬的yrhjrj，花了97ms更慢
        N1, N2 = len(num1), len(num2)
        ans = [0]*(N1+N2) # 這個陣列用來存整數的答案
        for i in range(N1): # 直式乘法
            for j in range(N2): # 直式乘法
                ans[1+i+j] += int(num1[i])*int(num2[j])
        for i in range(N1+N2-1,-1,-1): # 從低位往高位檢查
            if ans[i]>9: # 需要進位的話
                ans[i-1] += ans[i]//10 # 就進位
                ans[i] %= 10
        # print(ans)
        if ans[0]>0: # 最高位不是0
            return "".join(map(str,ans)) # 就直接轉成字串後，接起來
        else:
            # return "".join(map(str,ans[1:])) # 不行，換！
            for i in range(N1+N2):
                if ans[i]!=0: # 遇到0就一直避開，直到有非0的數
                    return "".join(map(str,ans[i:])) # 再轉成字串
            return "0" # 如果全部都是0的話，就回傳0吧
# case 302/311: "9133" "0" 會得到 "0000" 但是只能留個0
