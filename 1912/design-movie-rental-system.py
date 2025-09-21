# LeetCode 1912. Design Movie Rental System
# 設計「電影出租系統」以前「百視達、Netflix」有許多分店可租DVD
class MovieRentingSystem:

    def __init__(self, n: int, entries: List[List[int]]):
        self.price = defaultdict(int)  # (shop,movie)->price
        self.heapRented = []  # 已出租的片子，供 report()使用
        self.heapUnrented = defaultdict(list) # 還沒租出的片子，以movie分類，供search()使用
        self.rentedSet = set()  # 已租出去，用 (shop,movie) 當key
        for shop, movie, price in entries:  # 每家分店、每個電影「只有一片」價錢不同
            self.price[(shop,movie)] = price 
            heappush( self.heapUnrented[movie], (price, shop) )  # 「負號」變成「先找大的」

    def search(self, movie: int) -> List[int]:
        ans, backup = [], []  # ans 放 shop，backup 放回heap用
        while len(self.heapUnrented[movie]):  # 若不足、提早結束
            if len(ans)==5: break  # 湊齊5筆、提早結束
            price, shop = heappop( self.heapUnrented[movie] )
            if (shop,movie) in self.rentedSet: continue  # 若出租，換下一筆
            self.rentedSet.add((shop,movie))  # 暫時標記「已出租」
            backup.append( (shop,movie,price) )  # 備份
            ans.append(shop)
        for shop,movie,price in backup:  # 把「找到未出租」的「備份」放回 heap
            heappush( self.heapUnrented[movie], (price, shop) )
            self.rentedSet.remove((shop,movie))  # 將 暫時標記「已出租」變回「已歸還」
        return ans

    def rent(self, shop: int, movie: int) -> None:
        self.rentedSet.add( (shop,movie) )  # 供 search() 篩選用
        heappush( self.heapRented, (self.price[(shop,movie)], shop, movie) ) # 因 report()要用cheapest
        
    def drop(self, shop: int, movie: int) -> None:
        self.rentedSet.remove( (shop,movie) )
        heappush( self.heapUnrented[movie],(self.price[(shop,movie)], shop) )

    def report(self) -> List[List[int]]:  # 要湊 5 筆 heapRented 的資訊
        ans, backup = [], []  # ans 放 [shop,movie]
        while len(self.heapRented):  # 若不足、提早結束
            if len(ans)==5: break  # 湊齊5筆、提早結束
            price, shop, movie = heappop( self.heapRented)
            if (shop,movie) not in self.rentedSet: continue  # 若未出租，換下一筆
            self.rentedSet.remove((shop,movie))  # 暫時標記「已歸還」
            backup.append( (price,shop,movie) )  # 備份
            ans.append([shop,movie])
        for price,shop,movie in backup:  # 把「找到已出租」的「備份」放回 heap
            heappush( self.heapRented, (price, shop, movie) )
            self.rentedSet.add((shop,movie))  # 將 暫時標記「已歸還」變回「已出租」
        return ans


# Your MovieRentingSystem object will be instantiated and called as such:
# obj = MovieRentingSystem(n, entries)
# param_1 = obj.search(movie)
# obj.rent(shop,movie)
# obj.drop(shop,movie)
# param_4 = obj.report()
