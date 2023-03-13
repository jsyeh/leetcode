class Solution {
public:
    string convert(string s, int numRows) {
        if(numRows==1) return s;
        string ans = "";
        char table[1000][1000]={};
        int i=0, j=0, down=1, N=s.length();
        for(int k=0; k<N; k++){
            table[i][j]=s[k];
            if(down==1){
                i++;
                if(i==numRows){
                    down=0;
                    i-=2;
                    j++;
                }
            }else{ //down==0
                i--;
                j++;
                if(i<0){
                    down=1;
                    i+=2;
                    j--;
                }
            }
        }
        int maxI=i, maxJ=j;
        for(int i=0; i<numRows; i++){
            for(int j=0; j<=maxJ; j++){
                if(table[i][j]!=0) ans += table[i][j];
            }
        }
        return ans;
    }
};
