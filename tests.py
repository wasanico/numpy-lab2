import numpy as np 


a = np.array([[0,-2,-6],
            [4,4,8],
            [-5,1,7]])
print(a)
b = np.compress(np.array([True]),a,axis =0)#retruns the first row for axis = 0 and if 1 for the col
print("b :",b)
c = np.compress((a>0)[0],a,axis=1)  
''' axis = 1 checks in the first row if any number >2 if yes then show all true col
((a>0)[0],a,axis=1)==> a>0 it checks if number is >0
                    ==> [0] and axis =1 it checks in row2 == the third
 '''
print(c)
c = np.compress((a>0)[:,1],a,axis=0)  #give any row where the middle column is greater than 0
print("next",c)
c = np.compress((a>0)[:,2],a) #when axis not specified its default to None
#we have a >0 in the last col since -6 is not true we don't see the 0 but 8 and 7 are both greater than 0 it will give us the last two
print(c)
c = np.compress((a>0)[:,1],a)#here the same but with the middle col
print(c)