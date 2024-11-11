// LeetCode 1213. Intersection of Three Sorted Arrays
// 找出 arr1 arr2 arr3 重覆的數
class Solution {
public:
    vector<int> arraysIntersection(vector<int>& arr1, vector<int>& arr2, vector<int>& arr3) {
        vector<int> ans;
        int i = 0, j = 0, k = 0;
        while(i<arr1.size() && j<arr2.size() && k<arr3.size()) {
            int smallest = min(arr1[i], min(arr2[j], arr3[k]));
            if(arr1[i]==arr2[j] && arr2[j]==arr3[k]){
                ans.push_back(arr1[i]);
            }
            if(arr1[i]==smallest) i++;
            if(arr2[j]==smallest) j++;
            if(arr3[k]==smallest) k++;
        }
        return ans;
    }
};
