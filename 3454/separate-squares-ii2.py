# LeetCode 3454. Separate Squares II
# squares[i] 有 [x,y,邊長] 想找一條橫線y 使得「上面面積==下面面積」要去除重疊
class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:
        events = sorted([(y,1,x,x+L) for x,y,L in squares] + [(y+L,-1,x,x+L) for x,y,L in squares] )
        activeIntervals = []  # 將 events 的區間，照 y 依序「增減」，events 就是y方向的「區間改變事件」
        prevY = events[0][0]  # 第1筆的y座標
        total = 0  # 全部區間的面積總和
        areaSegments = []  # 供第二次掃描「累積面積」用
        for y, diff, x0, x1 in events:  # 第一次掃描：照 y 依序「增減」
            if activeIntervals and y - prevY > 0:  # 已有x的區間，也有y改變量
                H = y - prevY  # y改變量：「高」
                activeIntervals.sort()  # 先排序，準備 merge interval
                W = prevStart = prevEnd = 0
                for start, end in activeIntervals:  # 第一次掃描：照 x 依序找「寬度」
                    if prevEnd < start:  # 分開
                        W += prevEnd - prevStart  # 增加的「寬度」
                        prevStart, prevEnd = start, end  # 算完後，新的變成「舊的」
                    else: prevEnd = max(prevEnd, end)  # 結合
                W += prevEnd - prevStart  # 離開上面迴圈，還缺「最後一段」補上
                total += W * H  # x方向掃描，得到的「total面積」
                areaSegments.append((prevY, W, H))  # 供第二次掃描「累積面積」用
            if diff>0: activeIntervals.append((x0,x1))  # 針對現在的 y 增減
            else: activeIntervals.remove((x0,x1))  # 針對現在的 y 增減
            prevY = y  # 針對現在的 y 增減後，要去處理下一段
        target = total / 2  # 全部面積的「一半」，是第二次掃描的目標
        for startY, W, H in areaSegments:  # 第二次掃描：要找全部面積的「一半」
            A = W * H  # 這次增減的面積
            if target - A <=0:  # target 會在這次用完，答案就在這一段
                return startY + (target / W)  # 加上 target 這次的高度改變
            target -= A  # 如果這次沒用完，繼續
