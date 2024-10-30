# LeetCode 941. Valid Mountain Array
# 確認 arr 是先增加、再減少，像山一樣
class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr)<3: 
            return False  # 長度不夠
        state = 0  # 先往上
        if arr[0]>=arr[1]:  # 先確認：開始是否變高。不是變高，就失敗
            return False 

        for i in range(1, len(arr)-1):
            if arr[i]==arr[i+1]: return False  # 相等，就失敗
            if state==0:  # 目前向上
                if arr[i]>arr[i+1]:
                    state = 1  # 變成向下
            else:  # 目前向下
                if arr[i]<arr[i+1]:
                    return False
        if state==1: return True
        else: return False
