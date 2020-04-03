from app.my_script import enlarge
#importing the function from the other file 

def test_enlarge():
    result = enlarge(3)
    assert result == 300
#thus is what happens if yiu feed in 3 - so the same thing should ahppen to whatever is fed in 
