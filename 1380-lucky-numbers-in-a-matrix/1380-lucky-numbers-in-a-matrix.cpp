class Solution {
public:
    vector<int> luckyNumbers(vector<vector<int>>& matrix) {
        vector<int> ans;

        int rows = matrix.size();
        int cols = matrix[0].size();

        for (int i = 0; i < rows; i++) {
            // Find minimum in current row
            int min = matrix[i][0];
            int col = 0;

            for (int j = 1; j < cols; j++) {
                if (matrix[i][j] < min) {
                    min = matrix[i][j];
                    col = j;
                }
            }

            // Check if it is maximum in its column
            bool lucky = true;

            for (int k = 0; k < rows; k++) {
                if (matrix[k][col] > min) {
                    lucky = false;
                    break;
                }
            }

            if (lucky) {
                ans.push_back(min);
            }
        }

        return ans;
    }
};