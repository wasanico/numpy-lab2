import numpy as np
import scipy as misc
"""
@author : Samelson Nicolas

The code solves any linear algebra problem within a 2 dimensional matrix and with x variables and y=x equations

"""

z=0
#prob = np.array([[3,2,6,9],[2,-5,7,10],[1,2,-4,0]])
prob = np.array([[1,2,3,4,5],[6,7,8,9,10],[3,5,6,4,2],[15,-3,6,7,0]])
#prob = np.array([[3,2,6],[2,-5,5]])
prob = prob.astype(float)
r,c = prob.shape
print(r,c)

if r>=c:
    print("too much equations for variables")
elif r+1!=c:
    print("too many variables for the equations")
elif r+1==c:
    for b in range (0,r):
        print("state",b+1)
        for a in range(b+1,r):
            prob[a] = prob[a][b]*prob[b]-prob[a]*prob[b][b] #solving with the euclidian system L1 = L1 * x2 - x1 * L2
        print(prob)
    for a in range(0,r):
        print("finding variables :",a+1)
        d = r - a -1
        x = 0                                               #for the first variable to find we use x= 0 so that it only does the quotient ==> see line 30
        for b in range(d,r-1):
            x+= prob[d][b+1]*prob[b+1][r]                   #creating a loop which can caluclate for each different row the previousely calclated variables to increment it in the one we're searching
        
        prob[d][r]=(prob[d][r]-x)/(prob[d][d])              #finding the variable by calculating : (independant term - all variables)/the number of its own variable
        prob[d][d]=1
        for e in range(d+1,r):
            prob[d][e] = 0
        print(prob)

for a in range(0,r):
    print("var",a+1,"=",prob[a][r])
    
        
        