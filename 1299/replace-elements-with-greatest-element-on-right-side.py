# 把每個格子，換成「它右邊最大的數」
# 反過來，先從右邊（往左逐步）建出「右邊最大的數」，再逐個更新即可
class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        rightBig = -1 # 從右往左走，目前最大數，將塞回arr中
        for i in range(len(arr)-1,-1,-1):
            now = arr[i] # 先備份「現在」的值，因等一下會被蓋掉
            arr[i] = rightBig # 把「目前」右邊最大值，放入arr[i]
            rightBig = max(rightBig, now) # 再更新 rightBig
        return arr
