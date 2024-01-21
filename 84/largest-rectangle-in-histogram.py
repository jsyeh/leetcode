# 我試著用 mono stack 實作看看
# 寫完後與dietpepsi 的solution比較，我好像寫得出來耶！
# 只是寬度的部分，我少寫個 -1 因為左邊界好像也不包含
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [-1] # 裡面放 height[i] 的 i 對應當時最小值
        # 依木桶理論,由最小值決定水桶的儲水高度、容量
        heights.append(0) # 最後的0幫助histogram高度清空
        # heights[-1] ... heights[index] ... heights[i]
        ans = 0
        for i2,h in enumerate(heights): # 逐項i2當右邊界
            # print('i2,h:',i2,h)
            while stack and h<heights[stack[-1]]:
                # monostack 裡，還有更小值，可繼續拆木條
                index = stack.pop() # 中間index，最短木條
                i1 = stack[-1] # 更左邊的 i1 當右邊界
                area = heights[index] * (i2-i1-1) # 高*寬
                #print('index:', index, 'i:',i1,i2, 'heights[index]:', heights[index], 'width:', i2-i1)
                ans = max(ans, area) # 更新看看最大面積
            stack.append(i2) # 每個人都有1次機會當主角
            # 所以就讓迴圈的右邊界i2塞進去當1次主角吧
            #print('stack', stack)
        return ans
