class Solution {
public:
    vector<string> letterCombinations(string digits) {
        return combination(digits, 0);
    }
    vector<string> combination(string digits, int start) {
        if(digits.length()==0){
            vector<string> ans;
            return ans;
        }
        //printf("start:%d\n", start);
        string table[] = {"", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"};
        if(start==digits.length()){
            vector<string> ans;
            ans.push_back("");
            return ans;
        }
        vector<string> ans;
        vector<string> sub = combination(digits, start+1);
        int d = digits[start]-'0';
        for(string list : sub){
            //cout<<list<<endl;
            for(int i=0; i<table[d].length(); i++){
                //printf(".");
                string temp = table[d][i] + list;
                ans.push_back(temp);
            }
        }
        //printf("return %d\n", start);
        return ans;
    }
};
