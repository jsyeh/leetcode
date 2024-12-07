// LeetCode 277. Find the Celebrity
// 找到「名人」，每個人都認識「名人」，但「名人」不認識任何人
// 只能呼叫 knows(a,b) 查看「誰是否認識誰」
class Solution {
public:
    int findCelebrity(int n) {
        int candidate = 0;
        for(int i=1; i<n; i++) {
            if(knows(candidate, i)) candidate = i;
        } // 最後會得到「唯一候選人」candidate
        int follower = 0; // 名人的跟隨者
        for(int i=0; i<n; i++) {
            if(i==candidate) continue;
            if(knows(i,candidate)) follower++;
            if(knows(candidate,i)) return -1; // 唯一候選人竟然認識別人，完蛋
        }
        if(follower==n-1) return candidate;
        return -1;
    }
};
/* The knows API is defined for you.
      bool knows(int a, int b); */
