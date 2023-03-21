class Solution {
    public int longestPalindrome(String s) {
        int [] H = new int[26+26];
        int N = s.length();
        for(int i=0; i<N; i++){
            char c = s.charAt(i);
            if(c>='A' && c<='Z') H[c-'A']++;
            if(c>='a' && c<='z') H[c-'a'+26]++;
        }
        int odd=0;
        int ans=0;
        for(int i=0; i<26+26; i++){
            if(H[i]%2==1) odd++;
            if(H[i]>=2) ans += H[i]/2*2;
        }
        if(odd>0) ans++;
        return ans;
    }
}
