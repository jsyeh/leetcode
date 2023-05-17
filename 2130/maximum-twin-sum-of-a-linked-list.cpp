/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    int pairSum(ListNode* head) {
        vector<int> a;

        ListNode * next = head;
        int N = 0;
        while(next!=nullptr){
            a.push_back(next->val);
            next = next->next;
            N++;
        }
        int ans = 0;//maximum twin sum
        for(int i=0; i<N/2; i++){
            int temp = a[i] + a[N-1-i];
            if(temp>ans) ans = temp;
        }
        return ans;
    }
};
