class Solution {
    int [] H;
    public int characterReplacement(String s, int k) {
        //題目分類sliding window + 2 pointer
        //可用 Histogram 分析，若雜訊超過k個，則左邊界右移
        // 10^5 *2 pointer * 26 字母
        H = new int[26];
        int left=0, right=0, ans=0, noise=0; //left有,right沒有
        while(true) {
            if(k>=noise) {
                H[s.charAt(right)-'A']++;
                right++;
            } else {
                H[s.charAt(left)-'A']--;
                left++;
            }
            noise = checkNoise(right-left);
            if(k>=noise && right-left>ans) ans = right-left;
            if(right==s.length()) break;
        } 
        return ans;

    }
    int checkNoise(int len) {
        int max=0;
        for(int i=0; i<26; i++){
            if(H[i]>max) max = H[i];
        }
        return len-max;
    }
}
