class Solution {
public:
    int makeConnected(int n, vector<vector<int>>& connections) {
        //數數有幾個 connected components, 便能知道要換幾根線
        int cables = connections.size();
        if(cables<n-1) return -1; //there are not enough cables
        vector<bool> visited(n);
        vector<vector<int>> neighbor(n);
        for(int i=0; i<cables; i++){
            int a = connections[i][0], b = connections[i][1];
            neighbor[a].push_back(b);
            neighbor[b].push_back(a);
        }

        int ccN = 0;//connected components Number
        for(int i=0; i<n; i++){
            if(visited[i]==false){
                ccN++;
                queue<int> Q;
                Q.push(i);
                visited[i]=true;
                while(Q.size()>0){
                    int next = Q.front();
                    Q.pop();
                    for(int k : neighbor[next]){
                        if(!visited[k]) {
                            Q.push(k);
                            visited[k]=true;
                        }
                    }

                }
            }
        }
        return ccN-1;
    }
};
//Case4: 11 [[1,4],[0,3],[1,3],[3,7],[2,7],[0,1],[2,4],[3,6],[5,6],[6,7],[4,7],[0,7],[5,7]]
//Case5: 8 [[0,2],[2,7],[5,7],[2,6],[1,3],[4,6],[1,2]]
