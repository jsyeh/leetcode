# LeetCode 2092. Find All People With Secret
# 「我只跟你講秘密哦！」八卦就這樣傳了出去。
# 要小心，同一個時間可能meeting有很多，會「馬上互享資訊」
class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        path = defaultdict(list)  # 秘密、八卦的傳輪路徑
        for a,b,t in meetings:  # 在 時間 t 可互傳八卦
            path[a].append( (t,b) )  # 要記得記下相見的時間
            path[b].append( (t,a) )  # 之後便能照著 t 的時間吐出來
        heap = []  # 知道秘密的heap，依照「時間t」處理
        heappush(heap, (0, firstPerson) )  # 第一個知道秘密的朋友
        heappush(heap, (0, 0) )  # 小心！Person 0 自己也會不小心講出秘密!
        ans = {0:0, firstPerson:0}  # 記錄「什麼時候」知道秘密
        while heap:  # 利用 heap 照時間 t 的先後處理
            t, person = heappop(heap)  # 現在 person 在時間 t 知道秘密
            if ans[person] < t: continue
            for t2, person2 in path[person]:
                if t2 < t: continue  # 時間無法逆轉，之前的meeting無效
                if person2 in ans and ans[person2] <= t2: continue  # 更早時，已處理
                ans[person2] = t2  # 記錄 person2 知道秘密的時間
                heappush(heap, (t2,person2) )  # 加入 heap 之後將再處理
        return list(ans.keys())  # 題目要以 list 回傳
