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
        print('Key' + str(coin))
        if coins[coin] > 0:
            print('inside if ' + str(coin))
            while amount >= coin:
                amount -= coin
                change.append(coin)
    return change
    


tests_are_equal(getChange(0), [])
tests_are_equal(getChange(1), [1])
tests_are_equal(getChange(2), [2])
tests_are_equal(getChange(3), [2,1])
tests_are_equal(getChange(5), [5])
tests_are_equal(getChange(6), [5,1])
tests_are_equal(getChange(7), [5,2])
tests_are_equal(getChange(55, { 50: 0, 20:20, 10: 20, 5: 20, 2: 20}), [20, 20, 10, 5])



# tests_are_equal(getChange(23), [20,2,1])
# tests_are_equal(getChange(80), [25,25,25,5])
# tests_are_equal(getChange(4, [1]), [1,1,1,1])
print("All clear")