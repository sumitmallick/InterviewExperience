import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;
import java.util.Queue;

class TreeNode {
    int val;
    TreeNode left, right;

    TreeNode(int item) {
        val = item;
        left = right = null;
    }
}

public class BinaryTreeLevelOrderTraversal {
    TreeNode root;

    public List<List<Integer>> levelOrderTraversal(TreeNode node) {
        List<List<Integer>> result = new ArrayList<>();
        if (node == null) {
            return result;
        }

        Queue<TreeNode> q = new LinkedList<>();
        q.add(node);

        while (!q.isEmpty()) {
            int levelSize = q.size();
            List<Integer> currentLevel = new ArrayList<>();
            for (int i = 0; i < levelSize; i++) {
                TreeNode currentNode = q.poll();
                currentLevel.add(currentNode.val);
                if (currentNode.left != null) {
                    q.add(currentNode.left);
                }
                if (currentNode.right != null) {
                    q.add(currentNode.right);
                }
            }
            result.add(currentLevel);
        }
        return result;
    }

    public static void main(String[] args) {
        BinaryTreeLevelOrderTraversal tree = new BinaryTreeLevelOrderTraversal();
        tree.root = new TreeNode(1);
        tree.root.left = new TreeNode(2);
        tree.root.right = new TreeNode(3);
        tree.root.left.left = new TreeNode(4);
        tree.root.left.right = new TreeNode(5);
        // tree.root.left.right.left = new TreeNode(10);
        // tree.root.left.right.right = new TreeNode(14);

        List<List<Integer>> traversalResult = tree.levelOrderTraversal(tree.root);

        for (List<Integer> level : traversalResult) {
            for (int val : level) {
                System.out.print(val + " ");
            }
            System.out.println();
        }
    }
}

// Time Complexity
// The time complexity of this code is O(n), where 𝑛 is the number of nodes in the binary tree.

// Space Complexity:
// The space complexity is also 𝑂(𝑛)
