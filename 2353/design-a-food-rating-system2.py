# 這題有點繁複，要做好多對照表。self.C2RF[cuisine] 是 heap 即 list, 可查 -最高分
# self.rating[food] 可查 food 最新評分
# self.f2C[food] 可查 food 對應的 cuisine 種類
# 所以要查 highestRated(cuisine): 會去查 self.C2RF[cuisine] 再取出 -最高分
# 但怕「舊評分」出錯，要先 heappop() 確認 self.rating[food] == rating 再推回去
class FoodRatings:

    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.F2C = defaultdict(str) # self.F2C['sushi']='japanese' 查食物的種類
        self.rating = defaultdict(int) # self.rating['sushi'] 查food的對應分數
        self.C2RF = defaultdict(list) # 「國家食物種類」對應的heap，裡放 (-rating, food)
        # self.C2RFheap['japanese'] 會是最低分(就是 -最高分) 日式食物對應 的名字

        for i in range(len(foods)):
            f, c, r = foods[i], cuisines[i], ratings[i]
            self.F2C[f] = c
            self.rating[f] = -r # 食物的評分， # 只有一開始用負的

            # 要用負的評分,前面「負分數」會排序，相同時，會再用後面的foods[i]排序
            heappush(self.C2RF[cuisines[i]], (-r,f) ) # 加入國家的食物種類

    def changeRating(self, food: str, newRating: int) -> None:
        self.rating[food] = -newRating # 只有一開始用負的
        heappush( self.C2RF[self.F2C[food]], (-newRating, food) )

    def highestRated(self, cuisine: str) -> str:
        while True:
            rating, food = heappop(self.C2RF[cuisine])
            if self.rating[food]== rating: # 分數正確，就回傳。(不對時，它會被丟掉)
                heappush(self.C2RF[cuisine], (rating, food)) # 正確的再擺回去
                return food

# 下面是前一次成功的答案
# Your FoodRatings object will be instantiated and called as such:
# obj = FoodRatings(foods, cuisines, ratings)
# obj.changeRating(food,newRating)
# param_2 = obj.highestRated(cuisine)
'''
# 給 食物food、種類cuisine、評分rating 完整資料
# 設計資料結構，方便查「種類cuisine」最高分，但麻煩的是「評分」可改
# 如果使用 heap 的話，雖然方便找最大值，但要怎麼更新其中一筆的值呢？
# 可在 heap 裡放舊、新資料。若 heappop() 的rating、food不合，就繼續下一筆
class FoodRatings:

    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.mapFoodRating = {} 
        # self.mapFoodRating['sushi'] 得到 rating
        self.mapFoodCuisine = {} 
        # self.mapFoodCuisine['sushi'] 得到 'japanese'
        self.mapCuisineHeap = {} 
        # self.mapCuisineHeap['japanese'] 對應 'japanese' 類最高 rating
        N = len(foods) # 3個list的長度都是N

        for i in range(N): # 將 list 內容逐項放到資料結構裡
            f, c, r = foods[i], cuisines[i], ratings[i]
            # 以下的 rating 都存負的，以便heap取出最出最負的值
            self.mapFoodRating[f] = -r # 負的rating
            self.mapFoodCuisine[f] = c
            # 下面會將 (-r, f) 存到對應的 heap 裡
            if c not in self.mapCuisineHeap:
                self.mapCuisineHeap[c] = [(-r, f)] 
            else:
                heappush(self.mapCuisineHeap[c], (-r,f) )

    def changeRating(self, food: str, newRating: int) -> None:
        self.mapFoodRating[food] = -newRating # 存負的 rating
        c = self.mapFoodCuisine[food] # 對應的種類
        heappush(self.mapCuisineHeap[c], (-newRating, food))

    def highestRated(self, cuisine: str) -> str:
        heap = self.mapCuisineHeap[cuisine]
        r, f = heappop(heap) # 抽最佳值
        while self.mapFoodRating[f] != r: # 若對應 rating 不對
            r, f = heappop(heap) # 繼續重抽
        # 離開迴圈，表示對應的 rating 正確時
        heappush(heap, (r,f)) # 再補回最佳的資料，不能遺失
        return f # 最佳的 food

# Your FoodRatings object will be instantiated and called as such:
# obj = FoodRatings(foods, cuisines, ratings)
# obj.changeRating(food,newRating)
# param_2 = obj.highestRated(cuisine)
'''
