class Solution {
public:
    vector<int> relativeSortArray(vector<int>& arr1, vector<int>& arr2) {
        int H[1001] = {};
        for(int i=0; i<arr1.size(); i++) {
            H[arr1[i]]++;
        }
        vector<int> ans;
        for(int i=0; i<arr2.size(); i++) {
            for(int k=0; k<H[arr2[i]]; k++) {
                ans.push_back(arr2[i]);
            }
            H[arr2[i]] = 0;
        }
        for(int i=0; i<=1000; i++) {
            for(int k=0; k<H[i]; k++) {
                ans.push_back(i);
            }
        }
        return ans;
    }
};
