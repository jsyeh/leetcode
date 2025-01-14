# LeetCode 2657. Find the Prefix Common Array of Two Arrays
# A 和 B 前 i 項裡，有幾個「共同」值，放在 ans[i] 
class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        setA, setB = set(), set()  # 看「有哪些數」在（前i項）裡
        ans = []
        total = 0  # 目前「有幾個數」是「共同」值
        for i in range(len(A)):
            setA.add(A[i])  # 新增加 A[i]
            setB.add(B[i])  # 新增加 B[i]
            if A[i] in setB: total += 1  # 多一個「共同」值
            if B[i] in setA and A[i] != B[i]: total += 1  # 再多一個「共同」值
            ans.append(total)  # 放入 ans 裡
        return ans
