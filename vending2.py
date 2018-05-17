from byotests import *


# eu_denominations = [200, 100, 50, 20, 10, 5, 2, 1]
eu = {200:20, 100:20, 50:20, 20:20, 10:20, 5:20, 2:20, 1:20}
# usa_denomination = [25, 10, 5, 1]
usa = {25: 20, 10: 20, 5:20, 1: 20}
usd_coins = [25, 10, 5, 1]

def getChange(amount, coins = eu):
    
    denomination = list(coins.keys())
    denomination.sort(reverse=True)
    
    change = []
    for coin in denomination:
        # print('Key' + str(coin))
            # You can get to the value in a dictionary using the square brackets. This if statement will make the function skip over the key if the value is zero. 
            while amount >= coin and coins[coin] > 0:
                amount -= coin
                coins[coin] = coins[coin] - 1 
                change.append(coin)
                
    if amount != 0: 
        return "No Change"
        
    print(coins[coin])    
    return change
    


tests_are_equal(getChange(0), [])
tests_are_equal(getChange(1), [1])
tests_are_equal(getChange(2), [2])
tests_are_equal(getChange(3), [2,1])
tests_are_equal(getChange(5), [5])
tests_are_equal(getChange(6), [5,1])
tests_are_equal(getChange(7), [5,2])
tests_are_equal(getChange(55, { 50: 0, 20:20, 10: 20, 5: 20, 2: 20}), [20, 20, 10, 5])
tests_are_equal(getChange(25, { 20: 0, 10:20, 5: 20, 2: 20}), [10, 10, 5])
tests_are_equal(getChange(50, { 20: 1, 10:0, 5: 1, 2: 1}), "No Change")



# tests_are_equal(getChange(23), [20,2,1])
# tests_are_equal(getChange(80), [25,25,25,5])
# tests_are_equal(getChange(4, [1]), [1,1,1,1])
print("All clear")