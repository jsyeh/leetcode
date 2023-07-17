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
        //先把 List 倒過來，以便從個位數開始加
        l1 = reverse(l1, nullptr);
        l2 = reverse(l2, nullptr);

        int carry=0;
        ListNode* t1 = l1;
        ListNode* t2 = l2;
        ListNode* ans = l1;
        while(t1!=nullptr || t2!=nullptr) {
            if(t1==nullptr) {
                ans = l2;
                t2->val = t2->val + carry;
                carry = t2->val / 10;
                t2->val = t2->val % 10;
                t2 = t2->next;
            } else if(t2==nullptr) {
                t1->val = t1->val + carry;
                carry = t1->val / 10;
                t1->val = t1->val % 10;
                t1 = t1->next;
            } else {
                t1->val = t1->val + t2->val + carry;
                carry = t1->val / 10;
                t2->val = t1->val = t1->val % 10;
                t1 = t1->next;
                t2 = t2->next;
            }
        }
        if(carry>0) {
            return new ListNode(1, reverse(ans, nullptr));
        } else return reverse(ans, nullptr);
    }
    ListNode* reverse(ListNode* list, ListNode* ans) {
        if(list==nullptr) return ans;
        ListNode* others = list->next;
        ListNode* now = list;
        now->next = ans;
        return reverse(others, now);
    }
};
//case 1113/1563: [5] [5]
