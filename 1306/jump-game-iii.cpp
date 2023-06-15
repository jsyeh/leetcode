class Solution {
public:
    queue<int> Q;
    bool canReach(vector<int>& arr, int start) {
        int visited[50000]={};

        Q.push(start);
        visited[start]=1;
        while(Q.size()>0){
            int i = Q.front();
            Q.pop();
            if(arr[i]==0) return true;
            if(i-arr[i]>=0 && visited[i-arr[i]]==0){
                Q.push(i-arr[i]);
                visited[i-arr[i]]=1;
            }
            if(i+arr[i]<arr.size() && visited[i+arr[i]]==0){
                Q.push(i+arr[i]);
                visited[i+arr[i]]=1;
            }
        }
        return false;
    }
};
