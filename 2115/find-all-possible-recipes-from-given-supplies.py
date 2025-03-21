# LeetCode 2115. Find All Possible Recipes from Given Supplies
# n 種食譜，recipes[i]需要的原料在 ingredients[i]裡。
# 目前提供 supplies 有許多原料，問能做出哪些 recipes[i]
# 註：做出來的 recipies[i] 也能變成新的 supplies 提供的原料
class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        can_do = defaultdict(list)  # 某個原料，可用來製作什麼？
        not_ready = defaultdict(list)  # 某個食譜，還差什麼原料
        for i in range(len(recipes)):
            for ingred in ingredients[i]:
                can_do[ingred].append(recipes[i])  # 原料 ingred 能做 recipes[i]
                not_ready[recipes[i]].append(ingred)  # 某個食譜「還差什麼原料」
        # 上面建「供給與需求」的資料結構，下面進行「提供原料」的模擬
        ans = []
        queue = deque(supplies)  # 將「已有的原料」變成 queue 先進先出
        while queue:
            supply = queue.popleft()  # 現在提供原料 supply
            for one in can_do[supply]:  # 可用來製作食譜 the one
                not_ready[one].remove(supply)  # 現在食譜 the one 不缺 supply 了
                if len(not_ready[one])==0:  # the one 沒有缺任何東西
                    ans.append(one)  # 可以做出來，加入答案
                    queue.append(one)  # 同時化身為「新原料」
        return ans
