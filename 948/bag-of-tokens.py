# 題目不好懂，但懂了之後「很簡單」
# 一開始 score是0， 只有 power
# 可以 power 換1分，也能1分換 power
# 所以，把tokens排序，數字左邊小、右邊大，
# 把power扣左邊的小power換分數，再把分數在右邊換大power
class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        tokens.sort()
        # 先儘量 power 換分數，換不到分數時，右邊再換到power
        ans = 0
        score = 0
        left, right = 0, len(tokens)-1
        while left<=right:
            while left<=right and power-tokens[left]>=0: 
                # 能換分數，就換分數
                score += 1
                ans = max(ans, score)
                power -= tokens[left]
                left += 1
            # 到這裡時，代表「沒辦法再換分數」只好將分數「改換power」
            if left<=right and score>0: 
                score -= 1
                power += tokens[right]
                right -= 1
            else: break
        return ans
# case 6/147: tokens = [26], power=51
