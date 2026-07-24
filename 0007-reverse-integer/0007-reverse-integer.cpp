class Solution {
public:
    int reverse(int x) {
        int n = 0;
        int y = 0;
        while( x != 0 )
        {
            
            y = x % 10;
            if( n > INT_MAX/10 || n == INT_MAX/10 && y > 7)
                return 0;
            if( n < INT_MIN/10 || n == INT_MIN/10 && y < -8)
                return 0;    
            n = n * 10 + y;
            x /= 10;
        }
        return n;

    }
};