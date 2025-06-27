# Time Complexity : O(n), where n is the number of nodes in the tree
# Space Complexity : O(n), for the queue used in BFS
# Did this code successfully run on Leetcode : Yes
# Any problem you faced while coding this : No

# Your code here along with comments explaining your approach

# I used BFS to traverse level by level and captured the last node at each level (rightmost)

from collections import deque

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        result = []
        queue = deque([root])

        while queue:
            level_size = len(queue)

            for i in range(level_size):
                node = queue.popleft()
                if i == level_size - 1:
                    result.append(node.val)  # Last node in this level
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

        return result
