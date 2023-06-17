//這題本來沒有頭緒，不過看了 Solutions 比較清楚知道要怎麼做
//https://leetcode.com/problems/make-array-strictly-increasing/solutions/377531/o-n-2-log-n-solution-starting-from-brute-force-improve-by-memoization/
//不過我雖然翻譯出程式並通過，但我還不太了解/沒辦法寫出來。慚愧！
class Solution {
public:
    int makeArrayIncreasing(vector<int>& arr1, vector<int>& arr2) {
        sort(arr2.begin(), arr2.end());
        int N1 = arr1.size(), N2 = arr2.size();
        int table[N2+1][N1];
        for(int i=0; i<N2+1; i++){
            for(int j=0; j<N1; j++){
                table[i][j]=INT_MAX;
            }
        }
        table[0][0] = INT_MIN;
        for(int i=0; i<=N2; i++){
            for(int j=0; j<N1; j++){
                if(table[i][j] == INT_MAX) continue;
                vector<int>::iterator it = upper_bound(arr2.begin(), arr2.end(), table[i][j]);
                if(table[i][j]>=arr1[j]){ //有找到
                    if(it!=arr2.end()){
                        if(j+1==N1) return i+1;
                        if(*it<table[i+1][j+1]) table[i+1][j+1] = *it;
                    }
                }else{
                    if(j+1==N1) return i;
                    if(arr1[j]<table[i][j+1]) table[i][j+1] = arr1[j];
                    if(it != arr2.end() && *it< arr1[j]){
                        if(*it<table[i+1][j+1]) table[i+1][j+1] = *it;
                    }
                }
            }
        }
        return -1;
    }
};
