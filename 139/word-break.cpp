class Solution {
public:
    bool wordBreak(string s, vector<string>& wordDict) {
        unordered_set<string> words(wordDict.begin(), wordDict.end());
        //將字典的字，都丟到 words 這個 hashset 裡

        int N = s.length();
        bool visited[N+1];
        for(int i=0; i<=N; i++) visited[i] = false;

        queue<int> Q;
        Q.push(0); //代表 s[0] 開頭
        while(Q.size()>0) {
            int a = Q.front(); //取出 開頭的位置，進行BFS找答案
            Q.pop();
            if(a==N) return true; //順利走到最後，很好

            for(int b = a+1; b<=N; b++){ //a...b...N 去看要斷在哪裡
                if(visited[b]){
                    continue; //這個有走過，可以不用再算
                }
                string now = s.substr(a, b-a); //a...b的字串長度是b-a
                if(words.find(now)!=words.end()) {
                    Q.push(b);
                    visited[b] = true;
                }
            }
        }
        return false; //沒能順利走到最後，結果 Queue清空，太慘了

    }
};
