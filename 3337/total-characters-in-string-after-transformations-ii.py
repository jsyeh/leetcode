# LeetCode 3337. Total Characters in String After Transformations II
# 將 s[i] 變成「接下來的」nums[s[i]-'a'] 個字母（'z' 之後會到回到 'a'）字母可能會越來越多
# 要做 t <= 10^9 次，讓這題「不能真的用迴圈模擬」，是「超級難的題目」
# 偷看 Solutions 裡 lee215 的解說，把繁複的運算，累積在26x26的矩陣裡，變成「矩陣乘法」
# 統計 s 的字母出現次數 freq，答案是 freq * (M 的 t 次方) 再（把每個字母的數目）逐項加起來
class Solution:
    def lengthAfterTransformations(self, s: str, t: int, nums: List[int]) -> int:
        def mat_pow(Mat, t):  # 矩陣 Mat 對自己乘 t 次（利用「函式呼叫函式」來拆解）
            if t==1: return Mat  # 1 次方，就是自己「本身」
            # 利用「二分法」每次切一半，讓 10^9 次運算，用「對稱」性質，大量減少計算
            half = mat_pow(Mat, t//2)  # 利用「函式呼叫函式」，取「一半」來乘
            ans = mat_mult(half, half)  # 兩個「一半」相乘，就還原成「全部」
            if t%2==1: ans = mat_mult(ans, Mat)  # 如果是奇數項，餘1次要再乘入
            return ans            
        MOD = 10**9+7  # 因答案太大，需取「餘數」
        def mat_mult(Mat1, Mat2):  # 兩矩陣相乘, IxK 矩陣 * K*J 矩陣，變成 IxJ 矩陣
            I, K, J = len(Mat1), len(Mat2), len(Mat2[0])  # for 迴圈的 3 個參數
            ans = [[0] * J for i in range(I)]  # 結果是 IxJ 矩陣
            for i in range(I):  # 橫的
                for j in range(J):  # 直的
                    for k in range(K):  # K 項
                        ans[i][j] += Mat1[i][k] * Mat2[k][j]  # 矩陣乘法的公式
                    ans[i][j] %= MOD  # 因答案太大，需取「餘數」
            return ans
        M = [[0] * 26 for i in range(26)]  # 建出 [26][26] 的矩陣
        for i in range(26):  # 矩陣乘法，是「橫的」乘「直的」，
            for j in range(i+1, i+nums[i]+1):  # 將 i+1 之後 nums[i] 個字母，都設成1
                M[i][j%26] = 1  # 這樣在矩陣乘法時，便能將「第i個數」蔓延出「一堆數」
        counter = Counter([ord(c)-ord('a') for c in s])  # 把 26種字母，換算成 0...25 的數
        freq = [[counter[i] for i in range(26)]]  # 變成對應的陣列 freq 向量
        ans = mat_mult(freq, mat_pow(M,t))  # 最後算出來的答案的矩陣，其中 ans[0] 有26個字母的出現次數
        return sum(ans[0]) % MOD  # 26個字母的出現次數「加起來」就是答案
