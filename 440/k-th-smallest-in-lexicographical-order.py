# LeetCode 440. K-th Smallest in Lexicographical Order
# 字母序從小到大，要找第k個數（從"1"開始，需要走k-1步）
# 與昨天題目相似，但不能用昨天字母「排序sort」來解，因k,n<=10^9太大
# 數字「字母序」有規律：像棵樹一樣，能往右、往下。同一層（位數相同）或走到下一層（位數增加1位）
class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        # 「從n1走到n2」，步數太多時，往下走；步數不夠時，繼續往右走
        def calSteps(n, n1, n2):  # 想知道「從n1走到n2」要幾步（總共n個數）
            steps = 0  # 一開始是0步，慢慢累積
            while n1 <= n:  # 超過 n 的數字不存在，就要結束。還沒超過，就一直做
                if n2 <= n: steps += n2 - n1  # 沒超過範圍，就要走相減的距離
                else: steps += n + 1 - n1  # 如果超過範圍，就走 n + 1 - n1
                n1 *= 10  # 考慮到下一層，多1位數
                n2 *= 10  # 考慮到下一層，多1位數
            return steps
        now = 1  # 從1開始，要往下一個數來數
        k -= 1
        while k > 0:  # 第k個數，要走 k-1 步
            # 「從now走到now」，步數太多時，往下走；步數不夠時，繼續往右走
            steps = calSteps(n, now, now+1)  # 現在位置 now 走到 now+1 經過幾步
            if steps <= k:  # 步數沒有超過「剩餘要走的總步數」
                now += 1  # 就可順利跳到 now + 1 
                k -= steps  # 同時扣掉「要經過幾步」
            else:  # 如果步數「不小心超過了」，那絕對不能走到 now + 1
                now *= 10  # 而是要往下走一層，位數增加
                k -= 1  # 往下走一層(ex. "1" 走到 "10" 或 "2" 走到 "20") 要用掉1步
        return now  # 最後「k步全部走完」離開迴圈，現在的數，就是目標（終點）
