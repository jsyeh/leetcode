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
    ListNode* sortList(ListNode* head) {
//        ListNode* temp = head;
//        while(temp!=NULL){
//            printf("->%d", temp->val);
//            temp = temp->next;
//        }
//        printf("\n");

        if(head==NULL) return head; //長度為0
        if(head->next==NULL) return head;//長度為1

        ListNode * fast = head;
        ListNode * slow = head;
        while(fast->next!=NULL && fast->next->next!=NULL){
            fast = fast->next->next;
            slow = slow->next;
        }

        ListNode * sorted1 = sortList(slow->next);
        slow->next = NULL;
        ListNode * sorted2 = sortList(head);

        //merge
        ListNode ans;
        ListNode * next = &ans;
        while(sorted1!=NULL && sorted2!=NULL){
            if(sorted1->val<sorted2->val){
                next->next = sorted1;
                next = next->next;
                sorted1 = sorted1->next;
            }else{
                next->next = sorted2;
                next = next->next;
                sorted2 = sorted2->next;
            }
        }
        if(sorted1==NULL) next->next = sorted2;
        else next->next = sorted1;

        return ans.next;
    }
};
