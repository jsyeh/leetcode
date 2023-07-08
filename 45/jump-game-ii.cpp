class Solution {
public:
    int jump(vector<int>& nums) {
        int N = nums.size();
        int table[N];
        for(int i=0; i<N; i++) table[i] = INT_MAX;

        table[0] = 0;
        for(int i=0; i<N; i++){
            for(int k=i+1; k<=i+nums[i] && k<N; k++){
                int temp = table[i] + 1;
                if(temp<table[k]) table[k] = temp;
            }
        }
        return table[N-1];
    }
};
