class Solution {
public:
    bool backspaceCompare(string s, string t) {
        string s2, t2;
        for(int i=0; i<s.length(); i++){
            if(s[i]=='#'){
                if(s2.length()>0) s2.erase(s2.length()-1, 1);
            }else{
                s2 += s[i];
            }
        }
        for(int i=0; i<t.length(); i++){
            if(t[i]=='#'){
                if(t2.length()>0) t2.erase(t2.length()-1, 1);
            }else{
                t2 += t[i];
            }
        }
        cout<<s2<<endl;
        cout<<t2<<endl;
        if(s2.compare(t2)==0) return true;
        else return false;
    }
};
//case 4: "y#fo##f" "y#f#o##f" 要小心殘留 # 的問題
