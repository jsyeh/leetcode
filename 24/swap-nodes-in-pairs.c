/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* swapPairs(struct ListNode* head){
    if(head==NULL || head->next==NULL) return head;
    struct ListNode* p1 = head;
    struct ListNode* p2 = head->next;
    while(p1!=NULL && p2!=NULL){
        int temp=p1->val;
        p1->val = p2->val;
        p2->val = temp;

        if(p1->next!=NULL) p1 = p1->next->next;
        else break;
        if(p2->next!=NULL) p2 = p2->next->next;
    }
    return head;
}
