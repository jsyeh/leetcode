# LeetCode 1346. Check If N and Its Double Exist
# 簡單題：「有沒有」arr[i] == 2 * arr[j] (i和j不能相同)
class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        N = len(arr)  # 數字只有500個
        for i in range(N):  # 直接暴力2層for迴圈即可
            for j in range(N):
                if arr[i] == 2 * arr[j] and i != j:
                    return True
        return False
