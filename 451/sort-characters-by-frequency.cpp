class Solution {
public:
    string frequencySort(string s) {
        int N = s.length();
        int H[62]={};//26+26+10
        for(int i=0; i<N; i++){
            if(s[i]>='A'&&s[i]<='Z') H[s[i]-'A']++;
            if(s[i]>='a'&&s[i]<='z') H[s[i]-'a'+26]++;
            if(s[i]>='0'&&s[i]<='9') H[s[i]-'0'+52]++;
        }
        char c[62];
        for(int i=0; i<26; i++) c[i] = 'A'+i;
        for(int i=0; i<26; i++) c[i+26] = 'a'+i;
        for(int i=0; i<10; i++) c[i+52] = '0'+i;

        string ans;
        ans.resize(N);
        for(int i=0; i<62; i++){
            for(int j=i+1; j<62; j++){
                if(H[i]<H[j]){
                    swap(H[i],H[j]);
                    swap(c[i],c[j]);
                }
            }
        }

        int len=0;
        for(int i=0; i<62; i++){
            for(int k=0; k<H[i]; k++){
                ans[len++] = c[i];
            }
        }
        return ans;
    }
};
