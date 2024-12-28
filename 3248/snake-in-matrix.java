// LeetCode 3248. Snake in Matrix
// n x n 的正方形（矩陣）一開始在左上角，commands 移動方向，問最後位置
class Solution {
    public int finalPositionOfSnake(int n, List<String> commands) {
        int i = 0, j = 0;
        for(String s : commands) {
            if(s.charAt(0) == 'U') i--;
            else if(s.charAt(0) == 'R') j++;
            else if(s.charAt(0) == 'D') i++;
            else j--;
        }
        return i * n + j;
    }
}
