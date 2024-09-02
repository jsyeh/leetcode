# LeetCode 1894. Find the Student that Will Replace the Chalk
# 有n位小朋友，輪流到黑板「用粉筆」寫題目，粉筆用量是 chalk[i]，
# 教室有 k 個粉筆，問第幾位小朋友「要寫但粉筆不夠用」，他就要去「補粉筆」
class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        N = len(chalk)
        k %= sum(chalk)  # 可針對最後一輪的「餘數」，直球對決
        for i, a in enumerate(chalk):  # 逐位小朋友模擬
            if k < a: return i # 粉筆不夠用，就是第i位小朋友！
            k -= a  # 這位小朋友「用掉了 a 個粉筆」k個粉筆又變少了！
        return 0
# 註：剛好把 chalk 用完的人，其實是「下一個人」才要去補粉筆
