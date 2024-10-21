#include <unordered_map>
#include <vector>

class Solution {
public:
    std::vector<int> twoSum(std::vector<int>& nums, int target) {
        // Create a hash map to store numbers and their indices
        std::unordered_map<int, int> num_map;
        
        // Loop through the numbers
        for (int i = 0; i < nums.size(); i++) {
            int complement = target - nums[i];  // Calculate the complement
            
            // Check if the complement exists in the map
            if (num_map.find(complement) != num_map.end()) {
                // If found, return the indices of the two numbers
                return {num_map[complement], i};
            }
            
            // If complement is not found, add the current number and its index to the map
            num_map[nums[i]] = i;
        }
        
        // Return an empty vector if no solution is found (though the problem guarantees one solution)
        return {};
    }
};
