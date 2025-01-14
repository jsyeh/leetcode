// LeetCode 2657. Find the Prefix Common Array of Two Arrays
// A 和 B 前 i 項裡，有幾個「共同」值，放在 ans[i] 
class Solution {
public:
    vector<int> findThePrefixCommonArray(vector<int>& A, vector<int>& B) {
        unordered_set<int> setA, setB; // 用 unordered_set 看「已加入」哪些數
        int total = 0, N = A.size(); // total 對應「有比對到」的數有幾個
        vector<int> ans(N); // 用來㫃答案
        for(int i=0; i<N; i++) { // 逐一檢視 A[i] 和 B[i]
            if(A[i]==B[i]) total++; // 兩個數相同，代表「都是第1次出現」，也一起出現
            else { // 兩數不同的話
                if(setA.count(B[i])) total++; // 可各測試1次
                if(setB.count(A[i])) total++;
            }
            setA.insert(A[i]); // 更新 setA 和 setB
            setB.insert(B[i]);
            ans[i] = total; // 更新答案
        }
        return ans;
    }
};
