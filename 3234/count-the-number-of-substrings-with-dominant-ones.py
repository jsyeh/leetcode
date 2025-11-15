# LeetCode 3234. Count the Number of Substrings With Dominant Ones
# s 字串裡「有幾種substring」裡面 (1的數量) >= (0的數量)的平方
# 這題標示 Medium，但「正確率只有1%」，很多人認為是 Hard 等級。
# substring 連續的片段，用「毛毛蟲」解。0不能太多，(0的數量)的平方「不能比sqrt(N)大」
class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        N = len(s)  # 字串長度
        ans = 0  # 累積「有幾種合格的substring」
        for z in range(int(sqrt(N))+1):  # Vlad 發現z的上限，逐一試每種z的上限
            old_ans = ans  # 這次z上限，若沒有答案，提早結束
            zeros = ones = 0  # 這次z上限，測試「毛毛蟲」體內 0 和 1 的數量
            tail = tail2 = 0  # 左邊尾巴，將拖著走
            for head in range(N):  # z 限制，進行「毛毛蟲」（右邊頭每次爬1格）
                if s[head]=='1': ones += 1  # 右邊頭吃到'1'
                else: zeros += 1  # 右邊頭吃到'0'
                while  zeros > z:  # '0'的數目，超過 z 的上限，就要開始「吐」
                    if s[tail]=='1': ones -= 1  # 左邊尾巴吐掉'1'
                    else: zeros -= 1  # 左邊尾巴吐掉'0'
                    tail += 1  # 左邊尾巴「往右縮」
                # 現在 zeros 數量，符合 z 的上限。專注處理「剛好」zero==z 的狀況
                if zeros == z and ones > 0 and ones >= zeros * zeros:  # 有解
                    tail2 = max(tail, tail2)  # 可大量減少 tail2 計算，避免重覆
                    while tail2 < head and s[tail2]=='1':  # 有多餘'1' 可吐掉
                        tail2 += 1  # 儘量縮看看，在「不動到'0'」的情況下，能縮幾格
                    ans += 1 + min(tail2 - tail, ones - zeros * zeros)  # 重要
                    # 符合 z 個 zeros 且「能減少的1的數量」且「減少的是公式中多餘的1」
            if ans == old_ans: break  # 這次z上限，若沒有答案，提早結束
        return ans
