# LeetCode 3160. Find the Number of Distinct Colors Among the Balls
# 球有有標籤 0..limit，每次 query (i,color)會「設定balls[i] 為色彩color」
# 問 queries[i] 時，球總共有幾種不同的色彩
class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        ans = []  # 將放 N 個答案
        balls = defaultdict(int)  # 「有標過」色彩的球
        counter = Counter()  # 統計「某個色彩」有幾個球
        for i,color, in queries:
            if i in balls:  # 這個球「曾標過」舊色彩
                old = balls[i]  # 舊色彩「將被換掉」
                counter[old] -= 1  # 舊色彩 -1
                if counter[old]==0:  # 若「舊色彩」沒有球了
                    del counter[old]  # 刪
            balls[i] = color  # 新的色彩，換上去
            counter[color] += 1  # 這個「新的色彩」球 +1
            ans.append(len(counter))  # 現在的球「有幾種色彩」
        return ans
