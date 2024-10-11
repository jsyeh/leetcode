# LeetCode 1942. The Number of the Smallest Unoccupied Chair
# 有n個朋友在 times[i] 進來、離開，會挑「index最小的空位」坐。請問 target朋友「會坐在哪個位子」？
# 可用「2個」Priority Queue (Heap)來實作：(1) 最小的空位 (2) 位子釋放的時間，再依sort後的時間模擬即可
class Solution:
    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:
        N = len(times)  # 有 N 位朋友會到訪
        friends = [(times[i][0],times[i][1],i) for i in range(N)]  # 照第i位「朋友」的時間，建「完整資訊」
        friends.sort()  # 「朋友」先照「到達時間」排序（排序時會先看 times[i][0] 的值，即「到達時間」）

        seats = []  # 建立 priority queue(heap)，會吐出「index最小的空位」
        releasing = []  # 照時間「釋放位置」，內含(leave離開時間,theSeat位置)，也是 priority queue(heap)
        for i in range(N):  # 朋友照著時間來訪
            heappush(seats, i)  # 多準備一個新位子（待命，不一定會用到）
            arrive, leave, friend = friends[i]  # 此時進來的朋友，他的「完整資訊」
            # 在arrive到達前，若有位子可放出來，就一直回收位子
            while len(releasing)>0 and arrive >= releasing[0][0]:  # releasing[0][0]是「釋放位置」的時間
                heappush(seats, heappop(releasing)[1])  # 回收的位子，拿來用
            theSeat = heappop(seats)  # 現在index最小的位子
            if friend==targetFriend: return theSeat  # 是 target朋友，就坐 theSeat位子
            heappush(releasing, (leave,theSeat))  # 記錄「朋友在leave時間離開時，會釋出的theSeat」
        return -1  # 其實這行不用寫啦，前面就會一定會找到位子。
