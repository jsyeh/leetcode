# LeetCode 2353. Design a Food Rating System
# 這是「資料結構」設計題，設計「食物評分系統」並完成「對應的函式」即可
# __init__() 負責初始化 foods食物名、cuisines哪一國料理、ratings初始評分（參數的英文都是複數）
# changeRating(食物,新分數)可修改評分，highestRated(哪一國料理)可查詢最高分的食物, heap可找最低/負最高分
class FoodRatings:

    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.system = defaultdict(str)  # 表格1: 食物 屬哪國料理/哪種菜系（因cuisines太難拼，改叫system菜系）
        self.rating = defaultdict(int)  # 表格2: 食物 的評分
        self.scoreboard = defaultdict(list)  # 表格3: 某國料理裡，分數「從高到低」
        for food,system,rating in zip(foods, cuisines, ratings):
            self.system[food] = system  # 表格1: 哪種菜系
            self.rating[food] = - rating  # 表格2: 原始評分（因 heap 關係，分數全變「負」的）
            heappush( self.scoreboard[system], (-rating, food) )  # 表格3: 分數「從高到低」

    def changeRating(self, food: str, newRating: int) -> None:
        self.rating[food] = -newRating  # （因 heap 關係，分數全變「負」的）
        system = self.system[food]  # （因cuisines太難拼，改叫system菜系）
        heappush( self.scoreboard[system], (-newRating, food) )  # 表格3:新的分數

    def highestRated(self, cuisine: str) -> str:
        # 要從 self.scoreboard[cuisine] 找到最高分數「而且分數是最新版分數」的食物
        scoreboard = self.scoreboard[cuisine]  # （因cuisines太難拼，改叫system菜系）
        while True:  # 持續做
            rating, food = scoreboard[0]
            if self.rating[food] == rating: break  # 評分符合，可離開 while 迴圈
            heappop(scoreboard)  # 沒離開迴圈，就「吐掉」錯誤評分、舊評分 的資料
        return food  # 找到最高分數「而且分數是最新版分數」的食物
