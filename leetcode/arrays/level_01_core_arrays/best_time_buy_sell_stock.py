prices = [7,1, 5,3, 6, 4]
# m=len(prices)
# i = 0
# j=m-1
  #! inititalize maxProfit to 0
def stock(arr):
    m=len(arr)
    i=0  
    max_profit = 0
    while i<m:
        j=m-1               #! resets j index to starting value  before the while loop
        while j>i:
            if arr[j]-arr[i]>0:
                profit  = arr[j]-arr[i]
                if profit> max_profit:
                    max_profit = profit
                               
                #! max_profit  compare previous profit with current profit , only store when current profit is higher
            j=j-1
        i=i+1
    return max_profit
#! suppose you buy on day 1 and sell on day to return 0 profit
#! reset an index after a loop means starting its value again from intial state
#! if resertting is your criteria than the index initialization must be placed after the loop
#!  Ask this question? Do I need to reset the pointer again from the starting point? If Yes then then place initialization within the loop
print(stock(prices))

