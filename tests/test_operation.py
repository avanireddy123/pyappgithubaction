from src.math_operations import add,sub 
# modular coding we imported add and sub functions from mathoperations

def test_add(): #this will be the test cases i'm gonna run over here
    assert add(2,3)==5 #assert is going to check whatever output i'm gonna get from this function is equal to the given num if yes it'll give me true
    assert add(-1,1)==0

#these are my unit test cases which i wanna execute

def test_sub():
    assert sub(5,3)==2
    assert sub(4,3)==1
    assert sub(3,3)==0
    assert sub(2,3)==-1
    
#i want my pytest library to check these test cases and see if its working fine wrt functions i've created (add, sub)