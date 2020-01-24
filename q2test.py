#q2test.py
#algorithms and data structures assignment 2019-20 q2
#matthew johnson 22 november 2019

#####################################################

import cProfile
from q2 import descendants

def q2test():
    assert descendants(1,2,1) == 1
    assert descendants(1,200,1) == 6
    assert descendants(1,200,2) == 2
    assert descendants(1,2000,3) == 33
    assert descendants(4000,6000,3) == 36
    assert descendants(123456,654321,20) == 4015
    assert descendants(1,1000000,59) == 402
    assert descendants(1,1000000,60) == 0
    print("All tests completed")

cProfile.run("q2test()")