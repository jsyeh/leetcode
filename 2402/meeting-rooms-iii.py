# meetings[i] = [starti, endi] 右不包含哦！
# 每個 starti 值都不同，代表不同時間開始
# 每次挑「房間號碼最小」的房間 0-index
# 房間有限，沒房間時，meeting要delay
# 「請問哪個meeting room」開最多會？
# 相同時，回傳「號碼較小」的房號
# 有 10^5 個 meeting，時間5*10^5
# 所以不能暴力模擬。根據 Hint 2 介紹「用兩個」priority queue
# 一個管「現在有空的room」以id排序
# 一個管「正在使用的room」以結束時間排序，放便照時間放出來
class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort() # 先照 start[i] 來排序
        roomEmpty = [] # 「現在有空的room」以id排序
        roomUsing = [] # 「正在使用的room」以結束時間排序
        counter = Counter() # 紀錄每個房間「使用次數」
        for i in range(n):
            heappush(roomEmpty, i) # 把全部的房間，都設定「有空」
            counter[i] = 0

        for start, end in meetings: # 針對每個 meeting 排序
            while len(roomUsing)>0 and roomUsing[0][0]<=start: # 有「可放出的房間」
                #print('roomUsing', roomUsing)
                heappush( roomEmpty, heappop(roomUsing)[1] ) # 放出，再放入roomEmpty
                # 上面這行要小心，要用 heappop() 不能用 pop()
            #print('roomEmpty', roomEmpty)
            #print('roomUsing', roomUsing)
            # 現在有空房間能用嗎？
            if len(roomEmpty)>0: # 有空房間能用
                roomid = heappop(roomEmpty) # 現在能用的房間
                heappush(roomUsing, (end,roomid))
                #print('現在的時間', start, '結束時間', end)
            else: # 若不幸「沒空房間」
                t, roomid = heappop(roomUsing) # 硬是拉一間「未來」最快有空的房間，拿來用
                heappush(roomUsing, (t+end-start, roomid)) # 標記「何時用完」及「房號」
                #print('現在的時間', t, '結束時間', t+end-start)
            counter[roomid] += 1 # 紀錄使用1次
            #print( start, end, 'roomid', roomid)
        #print(counter)
        #print(counter.most_common())
        #print(counter.most_common()[0])
        # 回傳 出現次數最多 .most_common() 的 roomid ，也就是 .most_common()[0]
        return counter.most_common()[0][0] # 但如果有很多都相同時，取最小的房號
# case 72/82: n=3, meetings=[[3,7],[12,19],[16,17],[1,17],[5,6]]
# case 81/82: n=100, meeting超多的，且結束時間「倒過來」
