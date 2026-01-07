# LeetCode 1603. Design Parking System
# 完成 class ParkingSystem 及 addCar() 函式
# 有三種大小的車位 big, medium, small
class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.lots = [0, big, medium, small]
        # 因 big:1, medium:2, small:3 所以最左邊再塞0

    def addCar(self, carType: int) -> bool:
        if self.lots[carType]<=0: return False  # 車位不夠，失敗
        self.lots[carType] -= 1  # 用掉1個對應大小的車位
        return True  # 成功


# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)
