from byotests import *

def getChange(amount):
    coins = [200, 100, 50, 20, 10, 5, 2, 1]
    change = []
   
    # if amount == 0:
    #     return []
    # if amount in coins: 
    #     return [amount]
        
    for coin in coins:         
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
tests_are_equal(getChange(4), [2,2])
tests_are_equal(getChange(23), [20,2,1])


print("All clear")