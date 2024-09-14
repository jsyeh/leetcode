# LeetCode 1229. Meeting Scheduler
# 兩人有空的時間不同，slots1[i]=[start, end] & slots2[i]=[start, end]
# 想找「一個」「最早」的開會時段：兩人都有空，且長度為duration
# Hint 2: 使用 two pointers 把「所有可能」都試過
class Solution:
    def minAvailableDuration(self, slots1: List[List[int]], slots2: List[List[int]], duration: int) -> List[int]:
        slots1.sort()  # 先把 slots 照「開始時開」排序好
        slots2.sort()
        p1, p2 = 0, 0  # pointer1 和 pointer2
        N1, N2 = len(slots1), len(slots2)
        while p1<N1 and p2<N2:
            start = max(slots1[p1][0], slots2[p2][0])
            end = min(slots1[p1][1], slots2[p2][1])
            if end-start >= duration:  # 這個 [start,end] 夠長
                return [start, start+duration]  # 就找到了
            if slots1[p1][1] > slots2[p2][1]:  # 以結束時間，決定「誰」往右移
                p2 += 1  # p1 比較後面，就 p2 右移
            else:
                p1 += 1  # p2 比較後面，就 p1 右移
        return []  # 找不到時段
