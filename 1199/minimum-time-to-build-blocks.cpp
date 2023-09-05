class Solution {
public:
    int N, split2;
    int minBuildTime(vector<int>& blocks, int split) {
        //從大到小排序
        sort(blocks.begin(), blocks.end(), std::greater<>() );

        N = blocks.size();
        split2 = split;
        //int table[N][N+1];
        vector<vector<int>> table(N, vector<int>(N+1, -1));

        return ask(0, 1, blocks, table);
    }
    //完成0...i blocks, 使用k workers
    int ask(int i, int k, vector<int>&blocks, vector<vector<int>>&table) {
        if(i==N) return 0; //終止條件:順利走到最後
        if(k==0) return INT_MAX; //終止條件:工人不夠用
        if(k>=N-i) return blocks[i]; //終止條件:有夠多的 worker
        if(table[i][k] != -1) return table[i][k]; //直接知道耗時多久
        //現在挑個 worker做blocks[i], 剩下繼續問
        int work_here = max(blocks[i], ask(i+1, k-1, blocks, table));
        //現在有花 split時間分兩群,工人k*2,上限N-i
        int split_here = split2 + ask(i, min(k*2, N-i), blocks, table);
        table[i][k] = min(work_here, split_here);
        return table[i][k]; //top-down解法，先0個blocks,1 worker
    }
};
