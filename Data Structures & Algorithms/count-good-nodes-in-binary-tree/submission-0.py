class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node, max_so_far):
            if not node:
                return 0

            good = 1 if node.val >= max_so_far else 0
            new_max = max(max_so_far, node.val)

            left = dfs(node.left, new_max)
            right = dfs(node.right, new_max)

            return good + left + right

        return dfs(root, float('-inf'))