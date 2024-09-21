// LeetCode 386. Lexicographical Numbers
// 將 1...n 的全部數字，「以字母序」排序好
class Solution {
public:
    vector<int> lexicalOrder(int n) {
        vector<string> a; // 使用 vector 容器（伸縮自如的陣列）
        for(int i=1; i<=n; i++) { // 將 1...n 逐一變成字串
            a.push_back(to_string(i)); // 再塞入陣列 a 裡面
        }
        sort(a.begin(), a.end()); // 利用 C++ 的 sort() 排序
        
        vector<int> ans; // 放答案的 vector 容器
        for(string s : a) { // 把「字串排序好」後，逐一取出「字串」
            ans.push_back(stoi(s)); // 再把字串用 stoi() 轉成整數，塞入答案
        }
        return ans;
    }
};
