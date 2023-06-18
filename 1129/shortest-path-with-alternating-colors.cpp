class Solution {
public:
    vector<int> shortestAlternatingPaths(int n, vector<vector<int>>& redEdges, vector<vector<int>>& blueEdges) {
        vector<vector<int>> graph1(n);//red
        vector<vector<int>> graph2(n);//blue
        for(vector<int> edge : redEdges){
            graph1[edge[0]].push_back(edge[1]);
        }
        for(vector<int> edge : blueEdges){
            graph2[edge[0]].push_back(edge[1]);
        }

        vector<int> ans(n, -1); //dist from 0 to i, default value is -1 (到不了)

        queue<int>Q1; //node index
        queue<int>Q2; //distance
        queue<int>Q3; //prev edge color: -1:unvisied, 1:red, 2:blue
        Q1.push(0); //node 0 是全部的起點
        Q2.push(0);
        Q3.push(-1); //-1: visited

        while(Q1.size()>0){
            int i = Q1.front(), dist = Q2.front(), c = Q3.front();
            Q1.pop(); Q2.pop(); Q3.pop();
            if(ans[i]==-1) ans[i] = dist; //沒來過的話
            //來過的話，就不用更新
//printf("i:%d dist:%d c:%d\n", i, dist, c);
            if(c!=1) //色彩不同
            for(int k=0; k<graph1[i].size(); k++){
                int next = graph1[i][k];
            //for(int next : graph1[i]){
                if(next!=-1) {//unvisied
                    Q1.push(next);
                    Q2.push(dist+1);
                    Q3.push(1);//1的下個色彩是2
                    graph1[i][k]=-1;//visited
                }
            }

            if(c!=2)
            for(int k=0; k<graph2[i].size(); k++){
                int next = graph2[i][k];
            //for(int next : graph2[i]){
                if(next!=-1) {
                    Q1.push(next);
                    Q2.push(dist+1);
                    Q3.push(2);//2的下個色彩是1
                    graph2[i][k]=-1;//visited
                }
            }
        }
        return ans;
    }
};
//case 36/90: 3 [[0,1]] [[1,2]]
