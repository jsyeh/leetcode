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
    ListNode* reverseList(ListNode* head) {
        if(head==nullptr) return nullptr;

        ListNode* ans = nullptr;
        ListNode* now = head;
        while(now!=nullptr){
            ans = new ListNode(now->val, ans);
            now = now->next;
        }
        return ans;
    }
};
