def newList(l):
   
    count = 0
    for v in l: 
        if v != 0 and v % 2 == 0:
             count +=1
    if count % 2 == 0 and count != 0:
            return True
    else: 
        return False 

# also can be written using "return count % 2 == 0" 

assert newList([3]) == False, "Odd number should return false"
assert newList([3,6,8]) == True, "Two even numbers should return True"
assert newList([2,5,4,6]) == False, "Three even numbers return false"
assert newList([]) == False, "Empty should return false"
assert newList([0]) == False, "Empty should return false"
assert newList([0,0,0,0,0])  == False, "Pass"


print("All Tests Pass")