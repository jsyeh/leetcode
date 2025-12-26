# LeetCode 2483. Minimum Penalty for a Shop
# customers[i] 第i小時'Y'有顧客、'N'沒顧客
# 若店家在第j小時關店休息，之前N沒人、之後Y有人，都是panelty
# 希望 panelty 越小越好，問「最早」可在何時關店休息？
class Solution:
    def bestClosingTime(self, customers: str) -> int:
        ans = 0  # 如果在第0小時關店休息
        minPanelty = panelty = 0  # 對應的基準設為0
        for i in range(len(customers)):
            if customers[i]=='Y':  # 恭喜，關店休息後，少1位客人撲空
                panelty -= 1  # 罰分減少
            else:  # 糟糕，這個小時沒客人，（這時開店營業）左邊變差了
                panelty += 1  # 罰分增加
            # 有了最新的 panelty 資訊後，這個 panelty 是否更小？
            if panelty < minPanelty:  # 更小的話，就可以更新
                ans = i+1  # 在 i+1 這個小時休息
                minPanelty = panelty  # 對應的 panelty 更小
        return ans
