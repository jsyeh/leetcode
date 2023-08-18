class Solution:
    def calculate(self, s: str) -> int:
        nums = [] # 裡面放一堆待加的數字，可用 append() 和 pop()
        op = "+" # 數字前的op運算符號。技巧：第一個數字，當成是 + 加法處理
        now = 0
        for i in range(len(s)):
            c = s[i]
            if c==" " and i!=len(s)-1: # 空格要避開，但結尾的空格又不能跳掉，因後面要運算
                continue

            if c.isdigit(): # 是數字
                now = now * 10 + int(c)
            
            # 遇到最後一位數 or 遇到運算符號，要清算前一項
            if not c.isdigit() or i==len(s)-1:
                # print(c)
                if op=="+": # 要 +now 
                    nums.append(now) # 這個數字加進去
                elif op=="-": # 要 -now
                    nums.append(-now) #
                elif op=="*": # 乘法很特別，要把前項取出來乘
                    now = nums.pop() * now
                    nums.append(now) # 乘好後，放回 stack
                elif op=="/": # 除法的處理，與乘法類似，但 -3//2會得到 -2 應要 -1
                    # now = nums.pop() // now 
                    now = int(nums.pop()/now) # 要改用這個才是整數除法
                    nums.append(now)
                op = c # 做完運算，更新 op 
                now = 0
            # print(nums)
        ans = 0
        for num in nums:
            ans += num
        return ans
# case 103/110: "14-3/2" 在最後 -3//2 竟會得到-2 就算錯了
# 在 Java -3/2 會是 -1 但在 Python -3//2 會是 -2
# 所以 不能用 nums.pop // now 而要改用 int(nums.pop()/now)
