class Solution {
public:
    vector<string> generateParenthesis(int n) {
        vector<string> ans;
        func(ans, "", n, 0, 0);
        return ans;
    }
    void func(vector<string> &ans, string now, int n, int left, int right) {
        if(left==right && right==n) {//數量完成正確，可以加到答案中
            ans.push_back(now);
        }

        if(left<n){ //還可再加左括號
            func(ans, now + "(", n, left+1, right);
        }

        if(left>right) { //還可再加右括號
            func(ans, now + ")", n, left, right+1);
        }
    }
};
