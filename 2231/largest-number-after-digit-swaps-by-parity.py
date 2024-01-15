# 可 swap 位置，讓數字越大越好
# (x) 只能 odd位置互換、even位置互換
# 是「奇數間」可互換、「偶數間」可互換
class Solution:
    def largestInteger(self, num: int) -> int:
        s = str(num) # 先變成字串，方便依奇位、偶位分開
        N = len(s)
        # 先把奇數位、偶數位「分開」
        evenItem = []
        oddItem = []
        for c in s: # 先照「奇數、偶數」的值 分群
            if int(c)%2==1: oddItem.append(c)
            else: evenItem.append(c)
        evenItem.sort() # 小到大排，之後 pop()會先取出大的
        oddItem.sort() # 小到大排，之後 pop()會先取出大的
        ans = []
        for c in s: # 再逐一檢查原本數字「奇數、偶數」的狀況
            if int(c)%2==1: ans.append(oddItem.pop())
            else: ans.append(evenItem.pop()) # 分別放回
        return int( ''.join(ans) ) # 再把數字串回來
        # 上面的程式才是對的
        ''' # 下面看錯。不是「奇數位」互換，是「奇數間」互換
        evenItem = [s[i] for i in range(0,N,2)]
        oddItem = [s[i] for i in range(1,N,2)]
        evenItem.sort(reverse=True) # 大到小排好
        oddItem.sort(reverse=True) # 大到小排好
        ans = []
        for i in range(N): # 再逐項接回
            if i%2==0: ans.append(evenItem[i//2])
            else: ans.append(oddItem[i//2])
        return int(''.join(ans)) # 把字母串起，再變回int
        '''

