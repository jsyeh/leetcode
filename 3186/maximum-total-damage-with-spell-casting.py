# LeetCode 3186. Maximum Total Damage With Spell Casting
# 魔法師有 N 種咒語，對應 power[i] 攻擊力，每種只能用一次
# 若用 power[i]，威力「強度相似」的咒語（減2、減1、加1、加2）就不能再用
# 「強度相似」不能用，但「強度相同」的可以用，問累積最大攻擊力。
class Solution:
    def maximumTotalDamage(self, power: List[int]) -> int:
        counter = Counter(power)  # counter[p] 對應「攻擊力p出現幾次」
        uniquePower = list(sorted(counter.keys()))  # Unique Power 裡面的「攻擊力」值都不重覆
        N = len(uniquePower)  # 有幾種「不同威力」的 power
        @cache  # 可用「函式呼叫函式」的 Dynamic Programming 來解
        def helper(i):  # 現在處理 uniquePower[i]，可用、可不用
            if i>=N: return 0  # 超過範圍、結束
            ans1 = helper(i+1)  # 不使用 uniquePower[i] 
            p = uniquePower[i]  # 現在想要使用 uniquePower[i]，改名「短一點」變數 p 
            ans2 = p * counter[p]  # 要使用 uniquePower[i], 目前 p * 出現次數
            for ii in range(1,4):  # 避開 p+1, p+2，可能是 i+1 or i+2 最多 i+3
                if i+ii < N and p + 2 < uniquePower[i+ii]:  # 順利避開相鄰 p+1, p+2
                    return max(ans1, ans2 + helper(i+ii))  # 就可用它
            return max(ans1, ans2)
        return helper(0)  # 從 uniquePower[0] 開始處理，往右逐一考慮
