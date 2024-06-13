public class ElementCounter {

    public static int countOccurrences(int[] arr, int x) {
        int firstOccurrence = findFirstOccurrence(arr, x);
        if (firstOccurrence == -1) {
            return -1;
        }

        int lastOccurrence = findLastOccurrence(arr, x);
        return lastOccurrence - firstOccurrence + 1;
    }

    private static int findFirstOccurrence(int[] arr, int x) {
        int low = 0, high = arr.length - 1;
        int result = -1;
        while (low <= high) {
            int mid = low + (high - low) / 2;
            if (arr[mid] == x) {
                result = mid;
                high = mid - 1;
            } else if (arr[mid] > x) {
                high = mid - 1;
            } else {
                low = mid + 1;
            }
        }
        return result;
    }

    private static int findLastOccurrence(int[] arr, int x) {
        int low = 0, high = arr.length - 1;
        int result = -1;
        while (low <= high) {
            int mid = low + (high - low) / 2;
            if (arr[mid] == x) {
                result = mid;
                low = mid + 1;
            } else if (arr[mid] > x) {
                high = mid - 1;
            } else {
                low = mid + 1;
            }
        }
        return result;
    }

    public static void main(String[] args) {
        int[] arr1 = {1, 1, 2, 2, 2, 2, 3};
        int x1 = 2;
        System.out.println(countOccurrences(arr1, x1)); // Output: 4

        int[] arr2 = {1, 1, 2, 2, 2, 2, 3};
        int x2 = 3;
        System.out.println(countOccurrences(arr2, x2)); // Output: 1

        int[] arr3 = {1, 1, 2, 2, 2, 2, 3};
        int x3 = 1;
        System.out.println(countOccurrences(arr3, x3)); // Output: 2

        int[] arr4 = {1, 1, 2, 2, 2, 2, 3};
        int x4 = 4;
        System.out.println(countOccurrences(arr4, x4)); // Output: -1
    }
}

// Time Complexity: 
// O(log n)
// Space Complexity: 
// O(1)