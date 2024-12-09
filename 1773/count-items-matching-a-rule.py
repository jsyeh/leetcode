# LeetCode 1773. Count Items Matching a Rule
# items[i] 裡有 [type, color, name] 資訊。
# 另有 ruleKey 和 ruleValue，請統計「符合rule」有幾個 items，
class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        ans = 0;
        for itemType, itemColor, itemName in items:
            if ruleKey=="type" and ruleValue == itemType: ans += 1
            elif ruleKey=="color" and ruleValue == itemColor: ans += 1
            elif ruleKey=="name" and ruleValue == itemName: ans += 1
        return ans
