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
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        ListNode* ans = new ListNode();
        ListNode* next = ans;
        ListNode* prev = nullptr;
        int carry = 0;
        while(l1!=nullptr || l2!=nullptr){
            int now = carry;
            if(l1!=nullptr){
                now+= l1->val;
                l1 = l1->next;
            } 
            if(l2!=nullptr){
                now+= l2->val;
                l2 = l2->next;
            } 
            next->val = now%10;
            next->next = new ListNode();
            prev = next;
            next = next->next;
            carry = now/10;;
        }
        if(carry!=0) next->val = carry;
        else prev->next = nullptr;
        return ans;
    }
};
