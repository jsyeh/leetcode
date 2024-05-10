# arr[i] 裡有 1 和一些質數，數字遞增、不重覆。它們可以「分子、分母」組成「分數」
# 問它們能做出的「第k小」的分數是誰，最後以[分子, 分母]來呈現。
# 數字有1000個，k是N*(N-1)/2 種可能。好像暴力算也行。
# 但參考 fun4LeetCode 寫的 solution 提到 Priority Queue 及 a/b vs. c/d 可用交叉相乘法
# 這裡使用 heap 來實作 Priority Queue 這個資料結構。
class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        heap = []
        N = len(arr)  # 一開始 arr 就排序好了(左小、右大), 可以直接用
        for i in range(N):  # 左小
            for j in range(i + 1, N):  # 右大, 所以要從 i+1 開始往右巡
                heappush(heap, (arr[i] / arr[j], arr[i], arr[j]))  # 會照第1個值, 從小到大排
        for kk in range(k):  # 依序取出 Priority Queue 裡前 k 小的數
            (v, a, b) = heappop(heap)  # 取出後, 會一直重覆放在 (v, a, b) 裡
        return [a, b]  # 第k次取出的數, 是第k小的數, 對應的 a, b 分別是分子、分母, 也就是答案
