# 要在 arr 裡, 把內容改掉, 但長度不變
# 遇到0時,把0重覆
# 為了加速, 不應該用兩層迴圈。最好只用一層迴圈
class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        # 先用最簡單的想法，浪費memory來做，應該最簡單
        N = len(arr)
        ans = [0]*N
        ansI = 0
        for i in range(N):
            if arr[i]==0:
                ansI += 1 # 再多往右移一格
            else:
                ans[ansI] = arr[i] # 複製值
            ansI += 1 # 一律往右移1格
            if ansI>=N: break # 放滿，提早離開
            
        # 接下來，再把 ans[i] 搬回 arr[i] 即可
        for i in range(N):
            arr[i] = ans[i]
        return
