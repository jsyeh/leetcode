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
    ListNode* oddEvenList(ListNode* head) {
        ListNode odd, even;
        ListNode * odd2 = &odd;
        ListNode * even2 = &even;

        while(true){
            if(head!=NULL){
                odd2->next = head;
                odd2 = odd2->next;
                head = head->next;
            }else break;
            if(head!=NULL){
                even2->next = head;
                even2 = even2->next;
                head = head->next;
            }
        }
        odd2->next = even.next;
        even2->next = NULL;

        return odd.next;
    }
};
