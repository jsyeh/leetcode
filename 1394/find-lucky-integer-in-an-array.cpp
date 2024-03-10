class Solution {
public:
    int findLucky(vector<int>& arr) {
        int H[501] = {};
        for(int i : arr) H[i]++;
        for(int i=500; i>0; i--) {
            if(H[i]==i) return i;
        }
        return -1;
    }
};
