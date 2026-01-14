# LeetCode 3454. Separate Squares II
# squares[i] 有 [x,y,邊長] 想找一條橫線y 使得「上面面積==下面面積」要去除重疊
class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:
        events = sorted([(y,1,x,x+L) for x,y,L in squares] + [(y+L,-1,x,x+L) for x,y,L in squares] )
        #events = []
        #for x,y,L in squares:
        #    events.append((y, 1, x, x+L))  # 在 y 增加一段x的區間
        #    events.append((y+L, -1, x, x+L))  # 在 y+L 減少一段x的區間
        #events.sort()  # 針對 y 小到大排序
        activeIntervals = []  # 將 events 的區間，照 y 依序「增減」
        prevY = events[0][0]  # 第1筆的y座標
        total = 0  # 全部區間的面積總和
        areaSegments = []
        for y, diff, x0, x1 in events:  # 照 y 依序「增減」
            if activeIntervals and y - prevY > 0:  # 已有x的區間，也有y改變量
                H = y - prevY  # y改變量：「高」
                activeIntervals.sort()  # 先排序，準備 merge interval
                W = prevStart = prevEnd = 0
                for start, end in activeIntervals:
                    if prevEnd < start:  # 分開
                        W += prevEnd - prevStart
                        prevStart, prevEnd = start, end
                    else: prevEnd = max(prevEnd, end)  # 結合
                W += prevEnd - prevStart
                total += W * H
                areaSegments.append((prevY, W, H))  #print('W', W, 'H', H, activeIntervals)
            if diff>0: activeIntervals.append((x0,x1))
            else: activeIntervals.remove((x0,x1))
            prevY = y
        target = total / 2  # print('total', total)
        for startY, W, H in areaSegments:
            A = W * H
            if target - A <=0:
                return startY + (target) / W
            target -= A
        #return 0
