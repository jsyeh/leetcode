class Solution {
    public int partitionString(String s) {
        //00:37 histogram 04:00錯誤卡住 05:47發現看錯題目了，是斷字
        /*int ans=0;
        int [] H = new int[26];
        for(int i=0; i<s.length(); i++){
            int c = s.charAt(i)-'a';
            H[c]++;
            if(H[c]>ans) ans = H[c];
        }
        return ans;*/
        int ans=0, i=0;
        while(i<s.length()){
            int [] H = new int[26];
            while(i<s.length()){
                int c = s.charAt(i)-'a';
                if(H[c]==0){
                    H[c]++;
                    i++;
                } else break;
            }
            ans++;
        }
        //if(i==s.length()) ans++;
        return ans;
    }
}//case 3: "hdklqkcssgxlvehva"
