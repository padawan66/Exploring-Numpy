import numpy as np

# ndarray in numpy is an n dimensional array which contains homogenous element ( of same datatype).

array = np.array([[2,3],[4,5]],np.int32)  # This is a two dimensional array with two rows and two columns
array = np.array([[7,5,4,3,5],[4,5,7,8,2],[1,4,3,5,6]])  # this is a two dimensional array with three rows and five columns

#The below random.random creates the matrices having random numbers
array = np.random.random((1,3,3,3,3)) 
# interpreting this - the first index always tells the number of rows 
# the above array has 1 row
# in that row there three sets
# with each set having  a set of three matrices
# with each matrix having 3 columns and three rows  (1,3,3,3,3) - Read from left to right
# visually represented as below

""" [[[[[0.09838387 0.9405899  0.02053033]
    [0.55689022 0.36568757 0.26689963]
    [0.1866536  0.81044547 0.18381118]]

   [[0.95273775 0.60772043 0.76869066]
    [0.19402804 0.60431147 0.23320649]
    [0.70289356 0.72237596 0.75282588]]

   [[0.22790101 0.24056491 0.01812613]
    [0.78793282 0.1924375  0.75557256] 
    [0.6220761  0.14789242 0.99131233]]]


  [[[0.93547495 0.31320892 0.98082512]
    [0.83671609 0.89506487 0.90438078]
    [0.80344537 0.06438346 0.78431586]]

   [[0.24888071 0.90176465 0.10198165]
    [0.83223228 0.9013208  0.18959497]
    [0.41499491 0.64346824 0.15696499]]

   [[0.84841377 0.50649337 0.92214841]
    [0.40982369 0.51825426 0.71289529]
    [0.31598659 0.94779077 0.17015172]]]


  [[[0.01281435 0.9061787  0.63355111]
    [0.73569196 0.45923398 0.82490536]
    [0.91824387 0.4368361  0.01190746]]

   [[0.06884379 0.93718908 0.96160218]
    [0.42390615 0.94744547 0.92053873]
    [0.12509312 0.81809885 0.29409855]]

   [[0.69210684 0.59563861 0.68168369]
    [0.50215109 0.80389318 0.18381437]
    [0.14290239 0.85765904 0.27290198]]]]] """
print(array)