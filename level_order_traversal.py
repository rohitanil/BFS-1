"""
TC -> O(n) where n is number of nodes
SC -> O(n). we have h keys in dictionary equal to number of levels but number of values
across all the keys will have a total of n elements.

Logic-> We use BFS as its a level order traversal. We maintain a hashmap to store the level and nodes in that level. As we
move to next level, we increment the level by 1
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        hm = defaultdict(list)

        def bfs(node, lvl):
            queue = [[node, lvl]]
            while queue:
                elem = queue.pop(0)
                curr_node, curr_level = elem[0], elem[1]
                if curr_node is not None:
                    hm[curr_level].append(curr_node.val)
                if curr_node.left:
                    queue.append([curr_node.left, curr_level + 1])
                if curr_node.right:
                    queue.append([curr_node.right, curr_level + 1])

        if root is None:
            return []
        bfs(root, 0)
        return list(hm.values())