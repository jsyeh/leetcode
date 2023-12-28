# 要在 arr 裡, 把內容改掉, 但長度不變
# 遇到0時,把0重覆
class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        N = len(arr)
        skip = 0 # 沒有要跳掉
        for i in range(N): 
            if skip>0: # 需要跳掉1格
                skip = 0 # 用完這次的 skop
                continue 
            if arr[i]==0: # 遇到0,要重覆
                for k in range(N-1, i, -1): # 倒著的迴圈
                    arr[k] = arr[k-1] # arr[k-1] 往後移
                skip = 1 # 下一格需要跳掉
        # 這個程式很沒有效率, 因為兩層迴圈要跑很久
