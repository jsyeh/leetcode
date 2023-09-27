# 看題目的描述，像是有名的 Turing Machine
# 讀到字母就寫字母，讀到數字就重覆整個tape
# 像 "a2345678999999999999999" 就把 a 重覆
# 2*3*4*5*6*7*8*9*9*9*9*9*9*9*9*9*9*9*9*9*9*9 共
# 8301530446056247680 次
# 如果當成模擬題去做，會遇到 tape/memory耗盡的問題
# 仔細觀察特質：(1)加到後面、(2)重覆，比Turing Machine簡單
# 模擬到長度超過 k 就不用再算。
# 再像stack一樣做解碼，回溯看最後一步是什麼操作，再回頭解決。
# 想到策略後，偷看 lee215的解題策略，和我相同耶！開心！
class Solution:
    def decodeAtIndex(self, s: str, k: int) -> str:
        length = 0 # length 是目前解碼長度，
        index = 0 # 解到上面長度時是對應的字串index
        for c in s:
            if c.isdigit(): length *= int(c) # 倍數長
            else: length += 1
            if length>=k: 
                break # 夠長了，離開迴圈
            index += 1 # 沒事的話，走到下一個index
            
        # 接下來倒著往回找tape上第k個字母是怎麼長出來的
        for i in range(index, -1, -1): # 倒著回找
            c = s[i] # 往回模擬時，現在在做的事
            if c.isdigit():
                length /= int(c) # 倒著回算原始長度
                k %= length # 等價於，回去查表比較小的k值
            else:
                if k==length or k == 0: 
                    # 這麼巧，剛好是這一格
                    return c
                length -= 1 # 長度變短一點
        return '' # 如果測試照規定，這行不會執行到

