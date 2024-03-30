# 可任意將「某段」反過來，做任意多次。問「能不能」將兩個陣列變成equal
# 我突然想到，「泡泡排序」就只要將「相鄰2數」交換，做很多次，就能排好序
# 所以，其實兩個陣列，照「相鄰2數」交換做多次，只要「內容一樣」就一定能 equal
# 問題突然簡化成：「counter是否一樣」
class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        counter1 = collections.Counter(target)
        counter2 = collections.Counter(arr)
        if counter1-counter2==collections.Counter():
            return True
        else: 
            return False
