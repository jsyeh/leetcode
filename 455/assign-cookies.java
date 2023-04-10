class Solution {
    public int findContentChildren(int[] g, int[] s) {
        Arrays.sort(g);
        Arrays.sort(s);

        int ans = 0;
        int k = s.length-1;
        if(k<0) return 0;
        for(int i=g.length-1; i>=0; i--){
            if(s[k]>=g[i]){
                ans++;
                k--;
                if(k<0) break;
            }
        }
        return ans;
    }
}
