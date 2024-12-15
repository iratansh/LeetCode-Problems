/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* middleNode(struct ListNode* head) {
    struct ListNode* slowP = head;
    struct ListNode* fastP = head;

    while (fastP != NULL && fastP->next != NULL) {
        slowP = slowP->next;
        fastP = fastP->next->next;
    }

    return slowP;
}   
