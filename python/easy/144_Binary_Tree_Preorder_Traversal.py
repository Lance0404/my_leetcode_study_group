"""
https://leetcode.com/problems/binary-tree-preorder-traversal/

Given the root of a binary tree, return the preorder traversal of its nodes' values.

"""
from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def insert(root: TreeNode, val) -> TreeNode:
    if not root:
        return TreeNode(val)

    if not val:
        return root
        
    if val < root.val:
        print(f'insert {val} to left')
        root.left = insert(root.left, val)
    elif val > root.val:
        print(f'insert {val} to right')
        root.right = insert(root.right, val)
    else:
        print(f'how should we handle {val}?')
    return root        

class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        out = []
        stack = [root]
        while stack:
            """
            each itertion pop one, push two
            """
            node = stack.pop()
            print(f'node.val {node.val}')
            out.append(node.val)
            if node.right:
                print('add node.right')
                stack.append(node.right)
            if node.left:
                print('add node.left')
                stack.append(node.left)
        return out



if __name__ == '__main__':

    input = [1, None, 2, 3]

    root = insert(None, input[0])
    for i in input[1:]:
        root = insert(root, i)

    s = Solution()
    out = s.preorderTraversal(root)
    print(f'out {out}')

