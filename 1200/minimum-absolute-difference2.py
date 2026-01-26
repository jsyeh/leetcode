# LeetCode 1200. Minimum Absolute Difference
# arr 陣列裡「每個數都不同」，請列出一堆 pair 兩數相減的「絕對值」最小
class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()  # 先「小到大」排好
        target = min([arr[i+1]-arr[i] for i in range(len(arr)-1)])
        # 找到距離「絕對值」最小的 target
        ans = []
        for i in range(len(arr)-1):  # 再巡一次
            if arr[i+1]-arr[i]==target:  # 距離剛好是最小的target
                ans.append([arr[i],arr[i+1]])  # 加入ans
        return ans
