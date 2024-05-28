// LeetCode 1208. Get Equal Substrings Within Budget
// 兩個長度相同的字串 s, t，想找「最長的 substring」能在修改後相同。
// （修改需要 cost, 但能用的cost有上限）
// substring 是字串中「某段」連續的字母。可以利用 sliding window 解
// 技巧：像「毛毛蟲」一樣，頭（右邊）往右前進、尾（左邊）適時退縮。
int equalSubstring(char* s, char* t, int maxCost) {
    int ans = 0, i = 0, j = 0;  // 請把 i 想像成 head 頭，j想像成 tail 尾  
    for(int i=0; s[i]!=0; i++) { //字串的 for 迴圈，字串結尾是'\0'也就是0
        maxCost -= abs(s[i]-t[i]);  // 依字母距離，用掉部分 cost
        while(maxCost<0) {  // 如果不夠用、變成負的，只好尾巴縮短、從屁股還回去
            maxCost += abs(s[j]-t[j]);  // 尾巴能還回去的 cost
            j++;
        }
        if(i-j+1>ans) ans = i-j+1;  // 更新答案
    }
    return ans;
}
