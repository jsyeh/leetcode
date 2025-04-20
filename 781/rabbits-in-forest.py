# LeetCode 781. Rabbits in Forest
# 森林裡有不同色的兔子，問不同兔子「還有幾隻和你同色？」
# 請照 answers 的回覆，推理出「森林裡最少有幾隻兔子」
class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        counter = Counter(answers)  # 統計回答的數量
        ans = 0
        for c in counter:  # 齊聲回答 c 的可能同色，對應 c + 1 隻兔子
            # 可能有 c + 1 隻兔子，但若太多，要再分成幾群，每群 c + 1 兔子
            Q = counter[c] // (c + 1)  # 除法的商數
            M = counter[c] % (c + 1)  # 除法的餘數
            ans += (c + 1) * Q  # 可能有 Q 群
            if M > 0: ans += (c + 1)  # 但若有餘數，再加 1 群
        return ans
