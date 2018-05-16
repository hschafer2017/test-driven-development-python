from byotests import *

eu = [200, 100, 50, 20, 10, 5, 2, 1]
usa = [25, 10, 5, 1]

def getChange(amount, coins = eu):
    change = []
        
    for coin in coins:         
        while amount >= coin: 
            amount -= coin
            change.append(coin)
                
                
    return change    
                


tests_are_equal(getChange(0, eu), [])
tests_are_equal(getChange(1, eu), [1])
tests_are_equal(getChange(2, eu), [2])
tests_are_equal(getChange(3), [2,1])
tests_are_equal(getChange(5), [5])
tests_are_equal(getChange(6), [5,1])
tests_are_equal(getChange(7), [5,2])
tests_are_equal(getChange(4), [2,2])
tests_are_equal(getChange(23), [20,2,1])
tests_are_equal(getChange(80, usa), [25,25,25,5])
tests_are_equal(getChange(4, [1]), [1,1,1,1])

print("All clear")