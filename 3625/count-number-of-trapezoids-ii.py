# LeetCode 3625. Count Number of Trapezoids II
# 要找出 points 可組出的「所有梯形」。比前一題難，因「平行邊」沒限定方向
# Solutions 裡 Alex Wice 提出極巧妙的解法：用(dx,dy)斜率判斷「任2點的線段」平行，
# 用加法、減法考慮完所有可能，配合 Python itertools 排列組合，程式極精簡
class Solution:
    def countTrapezoids(self, points: List[List[int]]) -> int:
        sameSlope = Counter()  # 相同的斜率，會統計在一起，key是dx,dy
        sameLine = Counter()  # 相同的直線方程式，會統計在一起，key是dx,dy,x0截距
        # 上面2個，會與梯形有關（有2邊有「相同斜率」，但這2邊「不能共線」）
        # 下面2個，會與平形四邊形有關（「對角線」有相同的線段中心點，但「對角線」線段斜率不能相同）
        sameCenter = Counter()  # 相同的線段中心點，會統計在一起，key是x,y
        sameCenterSlope = Counter()  # 相同的線段中心點，而且線段斜率相同
        # 利用 itertools 的 combonatios 排列組合，把所有「挑2點」得「1線段」的可能都試過
        for (x1,y1),(x2,y2) in combinations(points, 2):  # 挑2點
            dx, dy = x2-x1, y2-y1  # 兩點相減，得到 dx, dy
            g = gcd(dx, dy)  # 需找「最大公因數」才能約分成「最精簡的形式」
            dx, dy = dx//g, dy//g  # 約分後，得到斜率「對應的dx,dy」
            if dx<0 or (dx==0 and dy<0):  # 遇到「正負號」時，讓分母為正，或斜率無限大時，dy為正
                dx, dy = -dx, -dy
            sameSlope[(dx,dy)] += 1  # 開心記下「相同斜率(dx,dy)」的量（統計在一起）
            c = dx * y1 - dy * x1  # 將(x1,y1)代入直線方程式dx * y = dy * x + c 算出x是0時的截距係數
            sameLine[(dx,dy,c)] += 1  # 開心記下「方程式完全相同」的線段，將會扣掉
            sameCenter[(x1+x2,y1+y2)] += 1  # 開心記下「可能構成平行四邊形」的「對角線中點」位置（不除2）
            sameCenterSlope[(x1+x2,y1+y2,dx,dy)] += 1  # 開心記下「無法構成平行四邊形」的對角線中點+斜率
        # 巧妙加減：梯形數 = 有兩相同平行邊，但要減掉「共線的平行邊」
        ans = sum([comb(v,2) for v in sameSlope.values()])  # math.comb(v,2) 從v個取2個=v*(v-1)//2 
        ans -= sum([comb(v,2) for v in sameLine.values()])
        # 但平行四邊形重覆算（要扣掉）= 對角線中點重疊 - 對角線中點（雖然）重疊但其實斜率相同、無法構成平行四邊形
        ans -= sum([comb(v,2) for v in sameCenter.values()])  # 要扣掉
        ans += sum([comb(v,2) for v in sameCenterSlope.values()])  # 要扣掉扣掉，負負得正
        return ans
