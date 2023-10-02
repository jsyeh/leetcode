class Solution:
    def numDifferentIntegers(self, word: str) -> int:
        table = set()
        word = re.split(r'[a-z]+', word)
        # 這是使用 regex 來進行斷字，不過會出現 '' 這個怪東西
        # print(word)
        for num in word:
            if num=='': continue # 把 '' 跳掉

            now = int(num) # 轉成數字
            if now not in table: # 如果數字沒出現過
                table.add(now) # 就加入 set 裡
        return len(table) # 回傳 set 的大小

