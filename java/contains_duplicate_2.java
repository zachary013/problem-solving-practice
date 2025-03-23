import java.util.HashMap;
import java.util.Map;

class contains_duplicate_2 {
    public boolean containsNearbyDuplicate(int[] nums, int k) {
        Map<Integer, Integer> map = new HashMap<Integer, Integer>();

        for(int i = 0; i < nums.length; i++) {
            if(!map.containsKey(nums[i])) {
                map.put(nums[i], i);
            }
            else {
                int diff = i - map.get(nums[i]);
                if(diff <= k) return true;
                else {
                    map.put(nums[i], i);
                }
            }
        }
        return false;

    }
}
