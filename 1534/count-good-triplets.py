# LeetCode 1534. Count Good Triplets
# arr 陣列中，挑選 arr[i] arr[j] arr[k]，3數間的距離要 <= a,b,c 問有幾組？
class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        N = len(arr)
        ans = 0
        for i in range(N):  # 就直接暴力3層迴圈，全部試過即可。
            for j in range(i+1, N):
                for k in range(j+1, N):
                    ii, jj, kk = arr[i], arr[j], arr[k]  # 多寫這行，讓下面別太長
                    if abs(ii-jj)<=a and abs(jj-kk)<=b and abs(ii-kk)<=c:
                        ans += 1  # 符合「距離不超過範圍」就 +1
        return ans        
