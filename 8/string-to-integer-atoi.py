class Solution:
    def myAtoi(self, s: str) -> int:
        ans = 0
        leading = True
        sign = 1
        for c in s:
            if leading and c==" ":
                continue
            # elif leading and c=="0":
            #     continue # 遇到 "0" 其實就開始計畫了，不再leading空白
            elif leading and c=="+":
                sign = 1
                leading = False
                continue
            elif leading and c=="-":
                sign = -1
                leading = False
                continue
            else: leading = False

            now = -1
            for i in range(10):
                if c == str(i): now = i
            if now==-1: break # 遇到不是數字的話，斷字結束

            ans = ans * 10 + now
        ans *= sign
        if ans > 2**31-1: return 2**31-1
        elif ans < -2**31: return -2**31
        else: return ans
# case 45/1086: "-91283472332" 遇到 overflow 怎麼辦？ 就給 INT_MAX 及 INT_MIN
# case 103/1086: "00000-42a1234" 在 leading zero 後面的 - 就斷開了
