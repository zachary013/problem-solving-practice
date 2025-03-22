
import java.util.HashMap;

class Solution {

    public int findPairs(int[] nums, int k) {
        HashMap<Integer, Integer> map = new HashMap<>();
        int count = 0;

        for (int num : nums) {
            map.put(num, map.getOrDefault(num, 0) + 1);
        }

        for (int item : map.keySet()) {
            if (k > 0 && map.containsKey(item + k)) {
                count++;
            }

            if (k == 0 && map.get(item) > 1) {
                count++;
            }
        }

        return count;
    }
}
