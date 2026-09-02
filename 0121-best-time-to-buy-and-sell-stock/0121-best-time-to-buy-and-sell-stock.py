class Solution:
    def maxProfit(self, prices: List[int]) -> int:
    
        buy_price = prices[0]
        profit = 0

        for p in prices[1:]:
            if buy_price > p:
                buy_price = p
            
            profit = max(profit, p - buy_price)
        
        return profit
        mini = prices[0]
        n=len(prices)

        for i in range(1,n):
            if prices[i] < prices[mini]:
                mini = i
        if mini == n-1:
            return 0
        maxi = prices[mini]    
        for j in range(i+1,n-1):
            if prices[i] > prices[maxi]:
                maxi = i