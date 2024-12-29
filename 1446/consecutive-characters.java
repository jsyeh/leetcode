// LeetCode 1446. Consecutive Characters
// 字串 s 裡，相同字母連續最長的長度
class Solution {
    public int maxPower(String s) {
        int ans = 1, prevN = 1;
        char prevC = s.charAt(0);
        for(int i=1; i<s.length(); i++) {
            if(s.charAt(i) == prevC) {
                prevN++;
                if(prevN > ans) ans = prevN;
            } else {
                prevC = s.charAt(i);
                prevN = 1;
            }
        }
        return ans;
    }
}
