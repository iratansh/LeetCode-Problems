/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */

bool helper(struct ListNode* listN, struct TreeNode* treeN) {
    if (!listN) {
        return true;
    } else if (!treeN || listN->val != treeN->val) {
        return false;
    }
    return (helper(listN->next, treeN->left) || helper(listN->next, treeN->right));
}

bool isSubPath(struct ListNode* head, struct TreeNode* root) {
    if (helper(head, root)) {
        return true;
    } 
    if (!root) {
        return false;
    }

    return (isSubPath(head, root->left) || isSubPath(head, root->right));
}
