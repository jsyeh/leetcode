class Solution {
public:
    int numOfMinutes(int n, int headID, vector<int>& manager, vector<int>& informTime) {
        //建出tree後,再去查tree的高度,就是答案。不過informTime[i] 也要再加上去, 再找 maxTime
        unordered_map<int, vector<int>> treemap;
        for(int i=0; i<manager.size(); i++){
            int m = manager[i];
//printf("manager: %d -> %d\n", m, i);
            if(m==-1) continue; //如果主管是-1表示它是老板, 沒有老板

            auto got = treemap.find(m);
            if(got!=treemap.end()){
                (got->second).push_back(i);
                //建出對應的tree, 也就是 manger m to 員工i
            }else{
                vector<int> children;
                children.push_back(i);
                treemap.insert( {m, children});
            }
        }

        return dfs(treemap, informTime, headID);
    }
    int dfs(unordered_map<int, vector<int>>& treemap, vector<int>& informTime, int headID) {
        int now = informTime[headID];//通知 headID 需要的時間

        auto children = treemap.find(headID);
        if(children == treemap.end()) return now;//沒有子節點
//沒有treemap的內容
//printf("headID: %d -- ", headID);
//for(int child : children->second){
//    printf("%d ", child);
//}
//printf("\n");

        int ans = INT_MIN;
        for(int child : children->second){
            int temp = dfs(treemap, informTime, child);
            if(temp>ans) ans = temp;
        }

        return now + ans;
    }
};
//case 2/39: 7 6 [1,2,3,4,5,6,-1] [0,6,5,4,3,2,1]
