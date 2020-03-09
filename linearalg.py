import numpy as np
import scipy as misc

z=0
prob = np.array([[3,2,6,2],[2,-5,7,5],[1,2,-4,-3]])
prob = np.array([[3,2,6],[2,-5,5]])
r,c = prob.shape
print(r,c)
if r ==1:
    x=0
elif r ==2:
    x=0
    y=0
elif r ==3:
    x=0
    y=0
    z=0
if r>=c:
    print("too much equations for variables")
elif r+1!=c:
    print("too many variables for the equations")
elif r+1==c:
    
    print("state 1 :\n",prob)
    for a in range(1,r):
        print("state",2,":")
        prob[a] = prob[a][0]*prob[0]-prob[a]*prob[0][0]
        print(prob)
    for a in range(2,r):
        print("state",3,":")
        prob[a] = prob[a][1]*prob[1]-prob[a]*prob[1][1]
        print(prob)
    """    
    if r ==1:
        x=prob[0][1]/prob[0][0]
        print("x =",x )
    elif r ==2:
        y=prob[1][2]/prob[1][1]
        x=(prob[0][2]-prob[0][1]*y)/prob[0][0]
        print("x =",x ,"y =",y)
    """    
    
        
    z=prob[r-1][r]/prob[r-1][r-1]
    y=(prob[r-2][r]-prob[r-2][r-1]*z)/prob[r-2][r-2]
    x=(prob[r-3][r]-prob[r-3][r-1]*z-prob[r-3][r-2]*y)/prob[r-3][r-3]
    print("x =",x ,"y =",y,"z =",z)

        
        