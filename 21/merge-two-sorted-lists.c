/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* mergeTwoLists(struct ListNode* list1, struct ListNode* list2){
    struct ListNode* ans = (struct ListNode*) malloc(sizeof(struct ListNode));
    struct ListNode* next = ans;
    while(list1!=NULL || list2!=NULL){
        if(list1!=NULL && list2!=NULL){
            if(list1->val <= list2->val){
                next->next = list1;
                list1 = list1->next;
            }else{
                next->next = list2;
                list2 = list2->next;
            }
            next = next->next;
        }else if(list1==NULL){
            while(list2!=NULL){
                next->next = list2;
                list2 = list2->next;
                next = next->next;
            }
        }else{
            while(list1!=NULL){
                next->next = list1;
                list1 = list1->next;
                next = next->next;
            }
        }
    }
    next->next = NULL; // 最後要收尾
    return ans->next;
}
