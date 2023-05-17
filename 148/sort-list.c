/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
void print(struct ListNode* head){
    while(head!=NULL){
        printf("%d ", head->val);
        head = head->next;
    }
    printf("\n");
}
struct ListNode* sortList(struct ListNode* head){
    //print(head);
    //只要能找到一半,便能將數字 divide & conquer 做出 merge sort
    if(head==NULL) return NULL;
    if(head->next==NULL) return head;

    struct ListNode* fast = head;
    struct ListNode* slow = head;
    while(fast->next!=NULL && fast->next->next!=NULL){
    //while(fast!=NULL && fast->next!=NULL){不能用這行,不然會切不平均
        fast = fast->next->next;
        slow = slow->next;
    }
    
    struct ListNode* list2 = slow->next;
    slow->next = NULL;

    struct ListNode * sorted1 = sortList(head);
    struct ListNode * sorted2 = sortList(list2);

    struct ListNode ans;
    struct ListNode * next = &ans;
    while(sorted1!=NULL && sorted2!=NULL){
        if(sorted1->val <= sorted2->val){
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
