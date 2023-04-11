class Solution {
    public int longestPalindrome(String s) {
        int [] H1 = new int[26];
        int [] H2 = new int[26];
        for(int i=0; i<s.length(); i++){
            char c = s.charAt(i);
            if(c>='A' && c<='Z') H1[c-'A']++;
            if(c>='a' && c<='z') H2[c-'a']++;
        }
        int ans=0;
        boolean odd=false;
        for(int i=0; i<26; i++){
            if(H1[i]%2==0) ans+=H1[i];
            if(H2[i]%2==0) ans+=H2[i];
            if(H1[i]%2==1){
                odd=true;
                ans+=H1[i]/2*2;
            }
            if(H2[i]%2==1){
                odd=true;
                ans+=H2[i]/2*2;
            }
        }
        if(odd) ans++;
        return ans;
    }
}
