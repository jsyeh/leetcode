// LeetCode 1346. Check If N and Its Double Exist
// 簡單題：「有沒有」arr[i] == 2 * arr[j] (i和j不能相同)
class Solution {
public:
    bool checkIfExist(vector<int>& arr) {
        int N = arr.size();
        for(int i=0; i<N; i++) {
            for(int j=0; j<N; j++) {
                if(arr[i] == 2 * arr[j] && i != j) return true;
            }
        }
        return false;
    }
};
