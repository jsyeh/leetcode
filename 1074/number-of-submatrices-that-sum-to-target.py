# 找出「有幾個」submatrix，加起來的sum是target
# 可利用「影像處理」常見的「積分圖」也就是「加總的結果」
# 便能快速算出submatrix的sum。
# 我稍卡住，參考 Solutions 裡 lee215下面haoyangfan的解釋
# 方法不太一樣，我是 now_sum = 右-左，他是 now_sum += 右-左，
# 因為我的 preSum 是方塊，他的 presum 是只有橫條狀
class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        M, N = len(matrix), len(matrix[0])
        preSum = [[0]*(N+1) for _ in range(M+1)]
        # preSum[i][j] : 不包含 matrix[i][j] 的左上角方塊和
        for i in range(1, M+1):
            for j in range(1, N+1):
                # 本格和 = 上+左-左上+本格
                preSum[i][j] = preSum[i-1][j] + preSum[i][j-1] - preSum[i-1][j-1] + matrix[i-1][j-1]
        print(preSum)
        # 但不能暴力算，因100^4 還是超過時間
        # 所以將其中一個迴圈，改用 hash table 加速
        ans = 0
        for j1 in range(1,N+1): # 左界（含）
            for j2 in range(j1, N+1): # 右界（含）
                counter = Counter()
                counter[0] = 1 # 都不用，就是0的這1種可能
                #now_sum = 0 # 最上面，什麼都沒有
                for i in range(1,M+1): # 下界（含）
                    # 在0..i這層，新增的一小段 j1..j2範圍
                    now_sum = preSum[i][j2] - preSum[i][j1-1]
                    # 精巧：「能湊到target」的組合「有多少」
                    # 也就是 now_sum - 之前 == target
                    # now_sum - target == 之前
                    ans += counter[now_sum - target]
                    # now_sum這個值，對應要多1個可能
                    counter[now_sum] += 1 
        return ans
