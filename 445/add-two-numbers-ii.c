/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* addTwoNumbers(struct ListNode* l1, struct ListNode* l2){
    int N1[100], N2[100], L1=0, L2=0;
    struct ListNode* temp = l1;
    while(temp!=NULL){
        N1[L1++] = temp->val;
        temp = temp->next;
    }
    temp = l2;
    while(temp!=NULL){
        N2[L2++] = temp->val;
        temp = temp->next;
    }

    int N3[102], L3=0;
    int carry=0;
    for(int i=0; i<L1 || i<L2; i++){
        N3[L3] = carry;
        if(i<L1) N3[L3] += N1[L1-1-i];
        if(i<L2) N3[L3] += N2[L2-1-i];
        if(N3[L3]>9){
            N3[L3] %= 10;
            carry = 1;
        }else carry = 0;
        L3++;
    }
    if(carry>0) N3[L3++] = carry;

    struct ListNode* ans = (struct ListNode*)malloc(sizeof(struct ListNode)*L3);
    for(int i=0; i<L3; i++){//}for(int i=L3-1; i>=0; i--){
        ans[i].val = N3[L3-1-i];
        if(i<L3-1) ans[i].next = &ans[i+1];
        else ans[i].next = NULL;
    }
    return ans;//struct ListNode * ans;
}
