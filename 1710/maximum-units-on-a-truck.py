# 想讓 Truck 裝最多Unit單位的東西。
# 每種 box 內含不同Unit單位。用greedy法應該就可以了
class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        # 先把 boxs 依 units 數目從大到小排好
        boxTypes.sort(key=lambda x: x[1], reverse=True) # 以 x[1]來 sort() 
        print(boxTypes) # 印出來確認

        ans = 0
        for boxs,units in boxTypes: # 由大到小，依序處理
            if truckSize >= boxs: # 卡車能全部載
                ans += boxs*units
                truckSize -= boxs # 空間變少
            else: # 卡車無法全部載
                ans += truckSize*units # 能裝多少裝多少
                return ans
        return ans
# case 40/76: [[1,3],[5,5],[2,5],[4,2],[4,1],[3,1],[2,2],[1,3],[2,5],[3,2]]
# 剛好截到最後離開，所以最後也要 return ans
