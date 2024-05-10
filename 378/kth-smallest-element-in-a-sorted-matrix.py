# 在矩陣裡，左到右 sort 好、上到下也 sort 好
# 想找到裡面第 k 小的數。總共有300x300＝9萬個數。
# 如果不顧一切，暴力把9萬個數「再sort一次」也可以找到答案
# 但如果能善用 row 與 col 都sort 的特質，可以更快。
# 因為趕時間、不太想思考，就用笨方法，使用 heap 把大家加入
# 再吐出第k小的數
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        M, N = len(matrix), len(matrix[0])
        heap = []
        for i in range(M):
            for j in range(N):
                heappush(heap, matrix[i][j])
        for k in range(k):
            ans = heappop(heap)
        return ans
