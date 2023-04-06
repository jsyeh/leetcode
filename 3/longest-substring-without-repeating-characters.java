class Solution {
    public int lengthOfLongestSubstring(String s) {
        int ans =0;
        int left=0, right=0;//右不包含
        int [] H = new int[256];
        while(right<s.length()){
            char c = s.charAt(right);
            while(H[c]==0){
                H[c]++;
                right++;
                if(right-left>ans) ans = right-left;
                if(right>=s.length()){
                    break;
                }
                c = s.charAt(right);
            }
            while(H[c]>0){
                char c2 = s.charAt(left);
                H[c2]--;
                left++;
            }
        }
        return ans;
    }
}
