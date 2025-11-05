# LeetCode 3321. Find X-Sum of All K-Long Subarrays II
# 題目似 3318 但「測資很大」變很難，不能再使用 sorted()函式。
# AI助手建議用兩個 SortedList 來存「長度k毛毛蟲」內的topX及全部
class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        freq = Counter(nums[:k])
        items = sorted([(f, num) for num, f in freq.items()])
        
        topX = SortedList(items[-x:] if len(items) >= x else items)
        others = SortedList(items[:-x] if len(items) > x else [])
        
        sumTop = sum(f * num for f, num in topX)
        ans = [sumTop]
        
        def rebalance():
            """確保 topX 有正確數量的最大元素"""
            nonlocal sumTop
            # 如果 topX 太少，從 others 提升
            while len(topX) < x and len(others) > 0:
                promoted = others.pop(-1)  # 取 others 最大的
                topX.add(promoted)
                sumTop += promoted[0] * promoted[1]
            
            # 如果 topX 太多，降級到 others
            while len(topX) > x:
                demoted = topX.pop(0)  # 取 topX 最小的
                others.add(demoted)
                sumTop -= demoted[0] * demoted[1]
            
            # 確保 topX[0] >= others[-1]（如果兩邊都有元素）
            while len(topX) > 0 and len(others) > 0 and topX[0] < others[-1]:
                # topX 最小的 < others 最大的，需要交換
                demoted = topX.pop(0)
                promoted = others.pop(-1)
                topX.add(promoted)
                others.add(demoted)
                sumTop += promoted[0] * promoted[1] - demoted[0] * demoted[1]
        
        def remove_element(num):
            nonlocal sumTop
            old_freq = freq[num]
            old_pair = (old_freq, num)
            
            if old_pair in topX:
                topX.remove(old_pair)
                sumTop -= old_freq * num
            else:
                others.remove(old_pair)
            
            freq[num] -= 1
            
            if freq[num] > 0:
                new_pair = (freq[num], num)
                # 先加到 others（保守做法）
                others.add(new_pair)
            else:
                del freq[num]
        
        def add_element(num):
            nonlocal sumTop
            
            if num in freq and freq[num] > 0:
                old_freq = freq[num]
                old_pair = (old_freq, num)
                if old_pair in topX:
                    topX.remove(old_pair)
                    sumTop -= old_freq * num
                else:
                    others.remove(old_pair)
            
            freq[num] = freq.get(num, 0) + 1
            new_pair = (freq[num], num)
            # 先加到 others
            others.add(new_pair)
        
        for i in range(k, len(nums)):
            remove_element(nums[i - k])
            add_element(nums[i])
            rebalance()  # ← 關鍵！每次操作後重新平衡
            ans.append(sumTop)
        
        return ans
