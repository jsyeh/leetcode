# LeetCode 2469. Convert the Temperature
# 溫度轉換：K = C + 273.15, F = C * 1.80 + 32.00
class Solution:
    def convertTemperature(self, celsius: float) -> List[float]:
        return [celsius + 273.15, celsius * 1.80 + 32.00]t
