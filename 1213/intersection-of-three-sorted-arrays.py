# 想找出 3 個 array 的 interaction，可使用 3 pointers
# 不過使用 set1 set2 再巡 arr3 可能會更簡單
class Solution:
    def arraysIntersection(self, arr1: List[int], arr2: List[int], arr3: List[int]) -> List[int]:
        set1 = set(arr1)
        set2 = set(arr2)
        ans = []
        for now in arr3:
            if now in set1 and now in set2:
                ans.append(now)
        return ans
