/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* countBits(int n, int* returnSize) {
    *returnSize = n + 1;
    int* result = (int*)malloc((*returnSize) * sizeof(int));

    result[0] = 0;  // Base case: 0 has 0 bits set
    for (int i = 1; i <= n; i++) {
        result[i] = result[i >> 1] + (i & 1);
    }

    return result;
}
