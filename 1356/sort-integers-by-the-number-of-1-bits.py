# 原本「想要用2個值來排序」好像很難，但sort()會有stable sort的特質
# 所以做「較不重要的小到大的 sort()」, 再做「以bit數為主」的sort()
# 這樣呈現的結果，便能「先以bit數為主」再以「較不重要的小到大的sort()」排序
class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        def helper(x)->int:
            one = 0
            while x > 0:
                one += x%2 # 如果是 1-bit 就會增加
                x //= 2 # 剝皮法
            return one # 會回傳 x 有幾個 1-bit

        arr.sort() # 先用傳統的 sort() 小到大排好
        arr.sort(key=helper) # 再做「以1-bit數為主」的sort()
        # stable sort 特質：若 1-bit 數相同，就照前面「小到大」順序，所以答案就會是對的
        return arr

