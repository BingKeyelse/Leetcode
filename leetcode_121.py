class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        min_price = float('inf') #Giá trị thấp nhất
        result =0 

        for price  in range(len(prices)):
            if price< min_price:
                min_price=price
            else:
                result= max(result, price - min_price)
           
        return result

        