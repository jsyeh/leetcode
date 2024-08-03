# 1460. Make Two Arrays Equal by Reversing Subarrays
# 可任意將「某段」反過來，做任意多次。問「能不能」將兩個陣列變成equal
# 我突然想到，「泡泡排序」就只要將「相鄰2數」交換，做很多次，就能排好序
# 所以，其實兩個陣列，照「相鄰2數」交換做多次，只要「內容一樣」就一定能 equal
# 問題突然簡化成：「counter是否一樣」
class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        if Counter(target) == Counter(arr):  # 如果統計出現次數都相同
            return True # 就能交換出來
        return False # 不相同時，就無法做出來
# 在 Python 3.10 後，兩個 Counter 的 == 比較，會更直覺。(LeetCode 用 Python 3.11)
