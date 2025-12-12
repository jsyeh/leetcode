# LeetCode 3433. Count Mentions Per User
# events[i] 可能是 (1) ["MESSAGE", "timestamp_i", "mentions_string_i"] 傳訊息
# (2) ["OFFLINE", "timestamp_i", "id_i"] 讓 id_i 關機60秒
# 請算出 mentions 陣列，裡面 mentions[i] 對應 user id 收到多少訊息
class Solution:
    def countMentions(self, numberOfUsers: int, events: List[List[str]]) -> List[int]:
        ans = [0] * numberOfUsers  # 用來放答案，對應 user i 收到多少訊息
        online = [0] * numberOfUsers  # 記錄 user i 在某個時間「是否開機」
        # 太過份了，因為 events 可能時間亂跳，所以要照時間「先排序」, 還要「先 OFFLINE 再 MESSAGE」
        events.sort( key = lambda e: (int(e[1]), 0 if e[0]=="OFFLINE" else 1))
        for event_type, t, ids in events:  # 模擬題，照著題目規則做
            t = int(t)  # 目前 events[i] 對應的時間
            if event_type=="MESSAGE":  # 要傳送訊息
                if ids=="ALL":  # 全部都送訊息
                    for i in range(numberOfUsers):  # 全部的 user
                        ans[i] += 1  # 傳送的訊息 +1
                elif ids=="HERE":  # 只針對「開機中」的 user 送訊息
                    for i in range(numberOfUsers):
                        if online[i] <= t:  # 目前「開機中」的user
                            ans[i] += 1  # 傳送的訊息 +1
                else:  # 只針對 ids 裡的 user
                    for id in ids.split():
                        ans[int(id[2:])] += 1
            else:  # 要關機60秒，一次只能挑「1台」機器
                online[int(ids)] = t + 60  # 關機60秒，所以t+60後，就開機了
        return ans
