# 奇數會變大、偶數會變小，所以可能的值，就是 奇數、變大。偶數、小到變奇數
# 想找到「全距最小」的值。Editorial 介紹2種很帥的方法。
# 第1種是：先拉到最大，再用 heap 把大的都變小。（所有大的值）小到不能再小，就找到答案了
class Solution:
    def minimumDeviation(self, nums: List[int]) -> int:
        N = len(nums)
        smallest = inf # 想找最小值，先放「無限大」
        h = [] # 供 heapq 使用的 heap，裡面放負的數
        for i in range(N):
            if nums[i]%2==1: # 奇數可放大
                nums[i] *= 2 # 先變兩倍，全偶數
            if nums[i]<smallest: smallest = nums[i] # 挑出最小值
            h.append(-nums[i]) # 等下 heapq會取用負數
        # 現在所有人都是偶數，可逐一找最大值，再把它變小哦！
        # google: python heap 可找到 heapq 它有 heapify(), heappush(), heappop()
        # https://weikaiwei.com/algorithm/heap/ 
        # https://docs.python.org/zh-tw/3/library/heapq.html
        # 不過 heapq.pop()會取出最小值，所以要反過來變 max heap，可把數字都變負的
        heapq.heapify(h)
        ans = inf # minimum deviation最小值, 先放「無限大」
        while True:
            now = - heapq.heappop(h) # 把最大值找出來(其實就是負的最小值，再負負得正)
            # 每次都用（現階段的）最大值，來更新 ans 值
            if now - smallest < ans: 
                ans = now - smallest

            if now %2 ==0:
                now //=2 # 把現在最大的數變小
                if now<smallest: smallest = now # 若大數變下界，那把smallest更新
                heapq.heappush(h, -now) # 再把次大值放回去 (因heapq關係，改放負數)
            else: # 若現在的最大值是奇數，那沒救了，程式結束
                break
        return ans

