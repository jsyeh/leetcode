# 想找出「得分最多」的 team, 其中 age 大的人，得分要多。
# 有人建議用 DP, Hint 1 建議照 age 排序
class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        N = len(scores)
        team = [[ages[i], scores[i]] for i in range(N)]
        team.sort(reverse=True) # ages 從大到小排，再照得分排序
        table = [0]*N
        for i in range(N): # 後輩 i
            # 我要使用 player i 時，得分最多是多少
            table[i] = team[i][1] # 先只看 player i 的得分
            for k in range(i): # 考慮 前輩 k (要得分比較多)
                if team[k][1]>=team[i][1]: # 前輩k 的得分多、後輩i 得分少
                    # 不會吵架，就可以組一隊，更新 table[i] 
                    table[i] = max(table[i], table[k] + team[i][1])
        return max(table)
