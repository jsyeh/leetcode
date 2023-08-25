# 找出數字ans，使得 arr[i] 裡比ans大的都變成ans的話，加起來最接近target
class Solution:
    def findBestValue(self, arr: List[int], target: int) -> int:
        arr.sort() # 先排序一下，以便之後binary search用
        N = len(arr)
        total = sum(arr)
        maxA = max(arr)
        if total < target: # 如果加起來還不夠大
            return maxA # 那要用現在的最大值

        prefix = [0]*(N+1) # 為方便計算，準備了 prefix[i]
        for i in range(1, N+1):
            prefix[i] = prefix[i-1] + arr[i-1]

        def mutateSum(value) -> int:
            left, right = 0, N
            while left<right: # 想知道哪個位置是value值
                mid = (left+right) //2
                if arr[mid] < value:
                    left = mid + 1
                else:
                    right = mid
            return prefix[left] + (N-left)*value

        left, right = 0, maxA
        while left<right:
            mid = (left+right) // 2
            # print(left, right, mid)

            m = mutateSum(mid)
            if m == target: return mid
            elif m < target:
                left = mid + 1
            else:
                right = mid
        # 找出結果時，要看哪個 abs(dist) 值最小
        a = mutateSum(left-1)
        b = mutateSum(left)
        # print(a, b, target) 
        # In case of a tie, return the minimum such integer.
        if target-a <= b-target: return left -1
        else: return left

        
