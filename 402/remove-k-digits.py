# 刪除k個字母後，可讓數字最小
# 另外 "0200" 要回傳 "200"
# 有 10^5 位數 所以不能暴力試
# 這題我沒什麼頭緒, 覺得有點難。所以看了 Solutions 裡 KnockCat 的解釋。
# 他使用的方法, 有點像 mono stack 的解法, 原則是: stack 裡, 數字會慢慢變大。
# 如果要吃的數字「突然變小」就代表它可以「在高位數的地方」擠掉大相對的數字。
# 總共可以擠 k 次, 後面就直接輸出即可。
class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = deque() # 換成 double end queue, 方便去除 leading zero
        for d in num:
            # 不需要轉成數字, 因為字母也能「比大小」
            while k>0 and len(stack)>0 and d < stack[-1]: # 可以擠掉最後1位的大的數
            # 還可擠掉數字, 且 stack 有數字, 且 現在數字更小, 就來擠掉吧
                k -= 1 # 擠掉1個數
                stack.pop()
            stack.append(d)

        # 因為 case 23/43 需要先把 leading zero 清光
        while k>0 and len(stack)>0: # 還能清的話 (被 test case 21/43, 16/42 騙到, 所以修正)
            stack.pop() # 最後的數, 沒有人能 pop 所以事後再 pop()
            k -= 1

        # 被 test case 14 騙到, 所以下面修正
        while len(stack)>0 and stack[0]=='0': # 可以清的 leading zero
            stack.popleft() # 去除左邊的 leading zero
        if len(stack)<=k: return "0" # 有殘留 k 可把 stack 清空的話, 就清為 0 並以字串 "0" 回傳
        #return str(int(''.join(stack))) # 先轉整數, 再轉字串, 可解決 leading zero 但被case 23打敗
        return ''.join(stack)

# case 14/43: num="9" k=1 可以擠掉數字哦!
# case 16/43: num="112" k=1
# case 21/43: num="1111111" k=3
# case 23/43: 超長的字串, 沒辦法 「轉成整數」(限定4300位數), 所以要處理
