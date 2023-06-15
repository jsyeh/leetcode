class Solution {
public:
    int minMutation(string startGene, string endGene, vector<string>& bank) {
        //想法:先建出 graph, 將gene bank 的資料建好
        //如果 endGene不在bank裡,就直接-1 (這個endGene就是最後目標)
        //再利用 BFS 去找距離
        int end = -1;
        for(int i=0; i<bank.size(); i++){
            if( endGene.compare(bank[i]) == 0) end = i;;
        }
        if(end == -1) return -1; //沒有找到 endGene 不合法, 直接-1

        int matrix[10][10] = {} ;
        for(int i=0; i<bank.size(); i++){
            for(int j=i+1; j<bank.size(); j++){
                if(isNeighbor(bank[i], bank[j])){
                    matrix[i][j] = matrix[j][i] = 1;
                }
            }
        }

        bool visited[10] = {};
        queue<int> Q; //queue
        queue<int> M; //mutate 次數
        for(int i=0; i<bank.size(); i++){
            if(isNeighbor(startGene, bank[i])) {
                Q.push(i);
                M.push(1);
                visited[i]=true;
            }
        }

        while(Q.size()>0){
            int now = Q.front(); 
            Q.pop();
            int m = M.front();
            M.pop();
            if(now==end) return m;

            for(int i=0; i<bank.size(); i++){
                if(visited[i] || matrix[now][i]==0) continue;
                Q.push(i);
                M.push(m+1);
            }
        }
        return -1;
    }
    bool isNeighbor(string a, string b) {
        int bad=0;
        for(int i=0; i<8; i++){
            if(a[i]!=b[i]) bad++;
        }
        if(bad==1) return true;
        else return false;
    }
};
//case 15/18: "AACCTTGG" "AATTCCGG"
//["AATTCCGG","AACCTGGG","AACCCCGG","AACCTACC"]
