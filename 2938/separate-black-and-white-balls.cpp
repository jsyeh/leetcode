// LeetCode 2938. Separate Black and White Balls
// 利用「相鄰兩球交換」將黑球'1'、白球'0'分開，問要「交換幾次」讓黑球在右、白球在左
// 看起來就是「泡泡排序法」，但 10^5 個球，不能真的 O(n^2) 去模擬
class Solution {
public:
    long long minimumSteps(string s) {
        long long ans = 0; // 已累積 swap 次數 （因數字加完會很大，需要 long long int）
        int black = 0; // 現在在處理的位置，左邊有幾個黑球'1' 需要跨越
        for(char c : s){ // 字串的迴圈
            if(c=='1') black++; //左邊又多了1個黑球（之後要跨越）
            else ans += black; // 球在是白球，那白球「要跨越黑球」到左邊集合
        }
        return ans;
    }
};
