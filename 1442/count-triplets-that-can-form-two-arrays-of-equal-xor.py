# 1442. Count Triplets That Can Form Two Arrays of Equal XOR
# 找到所有可能的 i,j,k 使得 arr[i]....arr[j-1] 全部 XOR 的結果,
# 與 arr[j]...arr[k] 全部 XOR 的結果, 會相同。
# 因 arr 有 300個數, 若用最暴力的迴圈 i,j,k 要跑300*300*300*(XOR累積的迴圈)300次, 可能太慢
# 幸運的是, 可善用 XOR 性質, 事先算出 prefix 表格, 查表(頭尾相差),省下XOR 的那個迴圈
# (這個程式很慢, 因用了3層迴圈)不過「啊我就慢/我就爛」反正容易理解, 寫得舒服就好 XD
# (高手會想要再加速, 運用一些數學性質, 讓迴圈可減成兩層迴圈, 就會更快了)
class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        N = len(arr)
        table = [0]  # table[i] 對應 arr[0]...arr[i-1] 全部 XOR 結果
        for i in range(N):
            table.append(arr[i] ^ table[i])  # 全部 XOR 在一起
        ans = 0
        for i in range(N):  # 挑選i (0 <= i < j <= k < arr.length)
            for j in range(i+1,N):  # 挑選j
                for k in range(j,N):  # 挑選k
                    # arr[i]...arr[j-1] 與 arr[j]...arr[k] 相同, 與下面的運算效果相同
                    if table[j]^table[i] == table[k+1]^table[j]:
                        ans += 1
        return ans
