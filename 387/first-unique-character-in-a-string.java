class Solution {
    public int firstUniqChar(String s) {
        //04:10重來
        int [] H = new int[26];
        for(int i=0; i<s.length(); i++){
            H[s.charAt(i)-'a']++;
        }
        for(int i=0; i<s.length(); i++){
            if( H[s.charAt(i)-'a']==1 ) return i;
        }
        return -1;
        /*int ans = -1;
        for(int i=1; i<s.length()-1; i++){
            if(i==1 && s.charAt(i)!=s.charAt(i-1)) return 0;
            if(s.charAt(i)!=s.charAt(i-1) && s.charAt(i)!=s.charAt(i+1)){
                ans = i;
                return ans;
            }
            if(i==s.length()-2 && s.charAt(i)!=s.charAt(i+1)){
                ans = i+1;
                return ans;
            }
        }
        return ans;*/
    }
}
