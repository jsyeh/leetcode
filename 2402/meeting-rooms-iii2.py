# LeetCode 2402. Meeting Rooms III
# n 間研討室(0..n-1) 用來開會 meetings[i] = [start[i],end[i]] （左包含、右不包含）
# 看開會選「編號最小」的「空房間」，若沒空房間就「順延時間」照順序「順延」最後「哪間房間」用最多次？（取編號最小的）
class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:        
        emptyRoom = [i for i in range(n)]  # 記錄「現在有空」的「空房間id」，待用（使用heap）
        heapify(emptyRoom)  # 變成 heap 資料結構，便能「每次取出id最小」的房間
        usingRoom = []  # 記錄「使用中」的房間「結束時間、id」，使用 heap 資料結構，便能「照結束時間」取出來
        counter = Counter()  # 記錄「房間」使用次數
        meetings.sort()  # 照「開始時間」小到大排序好
        for start, end in meetings:  # 依序開始開會
            while len(usingRoom)>0 and usingRoom[0][0] <= start:  # 開會前「使用中」房間「結束了」
                t2, room = heappop(usingRoom)
                heappush(emptyRoom, room)  # 變「空房間」
            # 準備「開始開會」囉！
            if not emptyRoom:  # 如果不幸「沒房間」，就要「順延時間」等「空房間」
                t2, room = heappop(usingRoom)  # 等一間「使用中」的房間，在t2「空出來」
                heappush(emptyRoom, room)  # 「空房間」待用
                end += (t2-start)  # 延後「開始時間」，也延後「結束時間」
            room = heappop(emptyRoom)  # 得到一個「空房間」
            counter[room] += 1
            heappush(usingRoom, (end, room))  # 記錄它「結束時間」
        ans = 0  # 想找「使用最多次」的房間。其實也能直接 return counter.most_common()[0][0]
        for c in counter:  # 在 counter 裡「逐一找」，其實也能用 
            if counter[c] > counter[ans]: ans = c  # 房間 c 使用次數更多，就更新
        return ans
