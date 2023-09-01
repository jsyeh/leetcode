class Solution {
public:
    int findMaximizedCapital(int k, int w, vector<int>& profits, vector<int>& capital) {
        int N = profits.size();
        vector<vector<int>> projects;
        for(int i=0; i<N; i++){
            vector<int> a;
            a.push_back(profits[i]);
            a.push_back(capital[i]);
            projects.push_back(a);
        }
        sort(projects.begin(), projects.end(), [](auto a, auto b) {return a[1] < b[1]; });
        //for(int i=0; i<N; i++){
        //    printf("(%d,%d) ", projects[i][0], projects[i][1]);
        //} 果然可以從小排到大
        priority_queue<int> heap;
        int i = 0; //對應 projects[i]
        while(k>0){ //還能做專案
            while(i<N && projects[i][1]<=w){
                heap.push(projects[i][0]);
                i++;
            }
            if(heap.size()==0) break; // 沒合適的專案能做，離開
            int earn = heap.top();
            //printf("earn:%d\n", earn);
            heap.pop();
            w += earn;
            k--;
        }

        return w;
    }
};
