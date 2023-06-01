/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* addTwoNumbers(struct ListNode* l1, struct ListNode* l2){
    struct ListNode* ans = l1;
    int carry = 0;
    while(l1!=NULL){
        l1->val += carry;
        if(l2!=NULL) l1->val += l2->val;
        if(l1->val > 9){
            carry = 1;
            l1->val %= 10;
        }else carry = 0;

        if(l1->next==NULL && l2!=NULL){ //l1不夠長, 就偷偷把 l2 後段接過來
            l1->next = l2->next;
            l2->next = NULL;
        }
        if(l1->next==NULL && carry>0){ //要結束了, 但還要多一位
            l1->next = (struct ListNode*) malloc(sizeof(struct ListNode)*1);
            l1->next->val = 0;
            l1->next->next = NULL;
        }
        l1 = l1->next;
        if(l2!=NULL) l2 = l2->next;
    }
    return ans;
}
