class Solution {
public:
    void nextPermutation(vector<int>& nums) {
    
        int n = nums.size();

        int i = n - 1;

        while (i > 0 && nums[i - 1] >= nums[i]) {
            i--;
        }

        if (i == 0) {
            int left = 0;
            int right = n - 1;

            while (left < right) {
                swap(nums[left], nums[right]);
                left++;
                right--;
            }
            return;
        }

        int j = n - 1;

        while (j >= i && nums[j] <= nums[i - 1]) {
            j--;
        }

        swap(nums[i - 1], nums[j]);

        int left = i;
        int right = n - 1;

        while (left < right) {
            swap(nums[left], nums[right]);
            left++;
            right--;
        }
    }
};
