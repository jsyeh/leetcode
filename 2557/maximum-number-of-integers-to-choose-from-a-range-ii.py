# 在 1..n 的範圍內，挑一堆數，不能超過 maxSum，不能挑banned
# 但是 n 最大到 10^9 所以迴圈會超時！ 所以要反過來，在 banned下手
class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        def area2h(area): # 這是將「梯形公式」由面積反推回「高」：「數字個數」
            return int((-1+(1+4*area)**0.5)//2) # 一元二次方程式的「根」
            
        banned = list(set(banned)) # 去除重覆的數
        banned.sort() # 從小到大排好，以便逐個分析
        runSum = 0 # 計算 banned 數字累積「數到哪裡？」
        for i,ban in enumerate(banned): # 逐個分析
            # 梯形公式：(上底+下底)*高//2 - banned
            runSum += ban # 前 i 項的sum
            area = (1+ban)*ban//2 - runSum
            if area > maxSum: # 超過，那不會用到 ban
                #print('inside')
                # 一樣用梯形公式，但反過來，由area算出邊界(高)
                return area2h((maxSum+runSum-ban)*2)-i # 扣掉「ban」對應個數
        N = len(banned)
        #print('outside')
        return min(n-N, area2h((maxSum+runSum)*2) ) # n不夠用 vs. 夠用（照公式）

        ''' # 以下程式會超時，所以重寫
        banned = set(banned) # 變成 set 會更快
        now = 0
        ans = 0
        for i in range(1,n+1):
            if i in banned: continue # 避開這些數
            now += i
            if now<=maxSum: ans += 1 # 多挑1個數
            else: break
        return ans
        '''
# caes 34/39: 有一大堆數字，n=1000000000, maxSum=405064161332609
