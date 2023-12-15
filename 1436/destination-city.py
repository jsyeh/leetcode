class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        City = set() # 這次會用到 Python 課本 3-4 集合 set()
        for a,b in paths: # 針對 path 裡 a,b 頭尾的2個城市
            City.add(a) # 每個城市都用 .add() 加到 City 這個集合
            City.add(b)

        for a,b in paths: # 這次打算把 City 中, 不是答案的 remove 掉
            City.remove(a) # .remove() 可以把裡面(不合格的)某個城市移陯
        
        print(City) # 把整個集合 印出來 觀察看看
        for ans in City: # 要怎麼取用 City 裡的值呢? 用 for 迴圈即可
            return ans
