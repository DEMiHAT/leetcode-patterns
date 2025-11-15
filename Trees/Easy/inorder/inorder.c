int* inorderTraversal(struct TreeNode* root, int* returnSize) {

    int* result = (int*)malloc(100 * sizeof(int));
    *returnSize = 0;
    
    struct TreeNode** stack = (struct TreeNode**)malloc(100 * sizeof(struct TreeNode*));
    int top = -1; 
    
    struct TreeNode* current = root;
    
    while (current != NULL || top != -1) {
        while (current != NULL) {
            stack[++top] = current;
            current = current->left;
        }
        
        current = stack[top--];
        result[(*returnSize)++] = current->val;
        current = current->right;
    }
    
    free(stack);
    return result;
}
