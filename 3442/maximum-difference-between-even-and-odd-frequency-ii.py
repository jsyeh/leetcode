class Solution:
    def maxDifference(self, s: str, k: int) -> int:
        ans = -inf
        for a in "01234": 
            for b in "01234": 
                if a != b: 
                    seen = defaultdict(lambda : inf)
                    pa = [0]
                    pb = [0]
                    ii = 0 
                    for i, ch in enumerate(s): 
                        pa.append(pa[-1])
                        pb.append(pb[-1])
                        if ch == a: pa[-1] += 1
                        elif ch == b: pb[-1] += 1
                        while ii <= i-k+1 and pa[ii] < pa[-1] and pb[ii] < pb[-1]: 
                            key = (pa[ii] % 2, pb[ii] % 2) 
                            diff = pa[ii] - pb[ii]
                            seen[key] = min(seen[key], diff)
                            ii += 1
                        key = (1 - pa[-1] % 2, pb[-1] % 2) 
                        diff = pa[-1] - pb[-1]
                        ans = max(ans, diff - seen[key])
        return ans 
'''
# LeetCode 3445. Maximum Difference Between Even and Odd Frequency II
# 0,1,2,3,4 這5種數字, 組合出字串 s, 找出 substring subs 長度至少 k 
# 希望 freq[某個出現奇數次的字母] - freq[某個出現偶數次的字母] 最大
# 遇到 substring 的問題, 或許「毛毛蟲」sliding window 的方法可解
# Hint 1 建議可「fix兩個字母」再利用 prefix sum 進行 sliding window 的解法
class Solution:
    def maxDifference(self, s: str, k: int) -> int:
        # 先建立 prefix sum 的陣列, 裡面有 0...4 的第2層陣列
        N = len(s)
        prefix = [[0] * (N+1) for d in range(5)]
        for i in range(N):  # 建立 prefix sum 陣列
            for d in range(5):  # 針對不同的字母，與s[i]相同，就+1
                if d==int(s[i]): prefix[d][i+1] = prefix[d][i] + 1
                else: prefix[d][i+1] = prefix[d][i]  # 不是s[i]就不動
        # 用毛毛蟲法，來解這題
        def helper(a,b):  # 給定 a b 兩字母,希望 a 出奇數次, b 出現偶數次
            tail = 0  # 左邊毛毛蟲尾巴
            for head in range(N+1):  # 右邊毛毛蟲的頭
                while head-tail >= k and (prefix[a][head]-prefix[a][tail])%2==0 or (prefix[b][head]-prefix[b][tail])%2==1:
                    

        ans = -inf  # 要找最大值，所以先設「最小最小」
        for a in range(5):  # 希望是奇數次數
            for b in range(5):  # 希望是偶數次數
                if a==b: continue  # 避開 a,b 是同一字母
                ans = max(ans, helper(a,b))  # 測 helper(a,b) 找到最大值
        return ans
'''
