# 題目寫 The start point of each interval is unique.
# 所以不可能會有兩個以上的 right interval (右邊的那個interval)
# 可以將 intervals 排序，再用 binary search 找到最適合的 start point
# 但排序會弄亂順序，所以需要在 interval 裡，加記「原本的index」
class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        N = len(intervals)
        end = []
        ans = []
        for i in range(N):
            intervals[i].append(i) # 所以 intervals[i][2] 是 index
            end.append(intervals[i][1]) # 記錄結束時間
        intervals.sort(key=lambda x: x[0])
        # print("new intervals:", intervals)
        # print("end:", end)
        for i in range(N): # 要逐一去測 end[i] 在哪裡
            left, right = 0, N
            while left<right:
                mid = (left+right)//2
                if end[i] <= intervals[mid][0]:
                    right = mid
                else:
                    left = mid + 1
            # print(left)
            if left < N and end[i] <= intervals[left][0]:
                ans.append(intervals[left][2])
            else:
                ans.append(-1)
        return ans
