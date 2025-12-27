# LeetCode 2402. Meeting Rooms III
# n 間研討室(0..n-1) 用來開會 meetings[i] = [start[i],end[i]] （左包含、右不包含）
# 借用「會議室房間」規則：每次借「編號最小」的房間，但沒空房間，就延後「直到有房間」
# 找到「使用次數最多」且「編號最小」的房間
class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        heapFree = list(range(n))
        heapify(heapFree)  # 用 heap 找「有空」的房間「編號最小」
        heapMeeting = []  # 正在開會使用的房間，會找到「結束時間」最早的 (t,room)
        counter = Counter()  # 統計「房間的使用次數」
        ans = 0  # 使用最多次的房間
        meetings.sort()  # 先照「開始時間」排序 
        for start, end in meetings:
            while heapMeeting and heapMeeting[0][0] <= start:
                t, room = heappop(heapMeeting)  # 開會前，就會有空的房間
                heappush(heapFree, room)  # 變成「有空」的房間
            if not heapFree:  # 如果不幸「沒有空房間」
                t, room = heappop(heapMeeting)  # 下一個空房間，在 t 出現
                end = end + (t - start)  # 開始時間延後 (t - start) 結束也延後
            else: room = heappop(heapFree) 
            heappush(heapMeeting, (end, room))  # 登記開會房間「結束的時間」
            counter[room] += 1  # 使用次數「加1」
            if counter[room] > counter[ans] or (counter[room]==counter[ans] and room<ans):
                ans = room  # 若使用次數更多 or 雖次數相同但編號更小，就更新答案
        return ans
