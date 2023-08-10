# 先利用 binary search 找到 pivot index
# 再利用 binary search 找 target
class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        N = len(nums)
        left, right = 0, N
        while left<right:
            mid = (left+right) // 2 # 整數除法得整數
            if nums[mid]== target: return True
            if nums[left]==nums[mid]:
                left += 1 # isBinarySearchHelpful()
                continue # 就偷偷調整邊界，就成功了
            if nums[0] < nums[mid]:
                left = mid+1
            else: right = mid
        pivot = left%N # 因為發現可能得到N，應該是0
        print(pivot)

        left, right = 0, N
        while left<right:
            mid = (left+right) // 2
            mid2 = (mid+pivot) % N # 換算 rotated 座標
            if nums[mid2]==target:
                return True # 找到了
            if nums[mid2]<target:
                left = mid + 1
            else:
                right = mid
        return False # 一直沒找到，可惜
# case 263/280: [1,1,1,1,1,1,1,1,1,1,1,1,1,2,1,1,1,1,1] 2 
# 這測資太難了，大海撈針，找到2？ binary search 找不到啊！
# 後來看 Editorial 解法，原來 isBinarySearchHelpful() 
#  可滑過去，避免前面有平滑的相同值，還蠻帥的
# case 265/280: [1,1,1,1,1,1,1,1,1,13,1,1,1,1,1,1,1,1,1,1,1,1] 13
# case 258/280: [1,1,1,1,1,1,1,1,1,13,1,1,1,1,1,1,1,1,1,1,1,1] 13
