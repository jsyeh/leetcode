class Solution {
public:
    int sumOddLengthSubarrays(vector<int>& arr) {
        int sum = 0;
        for(int i=0; i<arr.size(); i++) {
            for(int k=1; i+k<=arr.size(); k+=2) {
                for(int r=i; r<i+k; r++) {
                    sum += arr[r];
                    //printf("%d ", arr[r]);
                }
            }
        }
        return sum;
    }
};
