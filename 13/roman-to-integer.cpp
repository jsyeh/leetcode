class Solution {
public:
    int Table(char c) {
        if(c=='I') return 1;
        if(c=='V') return 5;
        if(c=='X') return 10;
        if(c=='L') return 50;
        if(c=='C') return 100;
        if(c=='D') return 500;
        if(c=='M') return 1000;
        return 0;
    }
    int romanToInt(string s) {
        int N = s.length();
        int prev=2000;
        int ans=0;
        for(int i=0; i<N; i++){
            int now = Table(s[i]);
            if(prev==1 && now==5) ans+=3; //1+3=4
            else if(prev==1 && now==10) ans+=8; //1+8=9
            else if(prev==10 && now==50) ans+=30; //10+30=40
            else if(prev==10 && now==100) ans+=80; //10+80=90
            else if(prev==100 && now==500) ans+=300;
            else if(prev==100 && now==1000) ans+=800;
            else ans+=now;
            prev = now;
        }
        return ans;
    }
};
