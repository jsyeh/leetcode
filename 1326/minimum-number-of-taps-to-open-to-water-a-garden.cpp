class Solution {
public:
    int minTaps(int n, vector<int>& ranges) {
        vector<int> table(n+1, INT_MAX);
        table[0] = 0;
        for(int i=0; i<=n; i++){
            int r = ranges[i];
            int left = max(0, i-r), right = min(i+r, n);
            for(int k=left; k<=right; k++){
                if(table[k] != INT_MAX && table[k]+1<table[right]){
                    table[right] = table[k] + 1;
                }
            }
        }
        if(table[n]==INT_MAX) return -1;
        return table[n];
    }
};
