class Solution {
public:
    int evalRPN(vector<string>& tokens) {
        int a[tokens.size()];
        int N = 0;
        for(int i=0; i<tokens.size(); i++){
            if(tokens[i].compare("+")==0){
                a[N-2] = a[N-2]+a[N-1];
                N--;
            }else if(tokens[i].compare("-")==0){
                a[N-2] = a[N-2]-a[N-1];
                N--;
            }else if(tokens[i].compare("*")==0){
                a[N-2] = a[N-2]*a[N-1];
                N--;
            }else if(tokens[i].compare("/")==0){
                a[N-2] = a[N-2]/a[N-1];
                N--;
            }else{
                a[N++] = stoi(tokens[i]);
            }
        }
        return a[0];
    }
};
