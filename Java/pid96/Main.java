package pid96;

/**
 * Unique Binary Search Trees 
 * 
 * Given n, how many structurally unique BST's
 * (binary search trees) that store values 1...n?
 * 
 * For example, Given n = 3, there are a total of 5 unique BST's.
 * 
 *  1         3     3      2      1
 *   \       /     /      / \      \
 *    3     2     1      1   3      2
 *   /     /       \                 \
 *  2     1         2                 3
 *  
 * @author 白
 *
 */

public class Main {
	public static void main(String[] args) {
		int[] testTable = { 0, 1, 2, 3, 4, 5, 6, 10 };
		for (int input : testTable) {
			test(input);
		}
	}

	private static void test(int input) {
		Solution solution = new Solution();
		int output;
		long begin = System.currentTimeMillis();
		output = solution.numTrees(input);
		long end = System.currentTimeMillis();
		System.out.println(input + ":	output=" + output);
		System.out.println();
		System.out.println("耗时：" + (end - begin) + "ms");
		System.out.println("-------------------");
	}
}

