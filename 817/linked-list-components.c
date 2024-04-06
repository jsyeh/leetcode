/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
int numComponents(struct ListNode* head, int* nums, int numsSize) {
    bool have[10001] = {};  // nums裡有存在的數
    for(int i=0; i<numsSize; i++){
        have[nums[i]] = true; // nums裡有存在的數
    }
    bool connected = false; // 目前 linked list 的數有無出現相連
    int ans = 0;
    while(head!=NULL){
        if(!connected && have[head->val]){
            connected = true; // 從無線有
            ans++;
        }else if(connected && !have[head->val]){
            connected = false; // 從有變無
        }
        head = head->next; // 下一筆
    }
    return ans;
}
