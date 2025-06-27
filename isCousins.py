# Time Complexity : O(n), where n is the number of nodes in the tree
# Space Complexity : O(n), for the queue used in BFS
# Did this code successfully run on Leetcode : Yes
# Any problem you faced while coding this : No

# Your code here along with comments explaining your approach

# I used BFS to track the parent and level of both nodes and checked if they are at the same level with different parents

from collections import deque

class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        queue = deque([(root, None)])

        while queue:
            x_parent = y_parent = None

            for _ in range(len(queue)):
                curr, parent = queue.popleft()

                if curr.val == x:
                    x_parent = parent
                if curr.val == y:
                    y_parent = parent

                if curr.left:
                    queue.append((curr.left, curr))
                if curr.right:
                    queue.append((curr.right, curr))

            if x_parent and y_parent:
                return x_parent != y_parent
            if x_parent or y_parent:
                return False
