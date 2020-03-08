import numpy as np
import scipy as misc

z=0
prob = np.array([[3,2,6,2],[2,-5,7,5],[1,2,-4,-3]])

r,c = prob.shape
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
        print("state",a+1,":")
        prob[a] = prob[a][0]*prob[0]-prob[a]*prob[0][0]
        print(prob)


    if r ==1:
        x=prob[0][1]/prob[0][0]
        print("x =",x )
    elif r ==2:
        y=prob[1][2]/prob[1][1]
        x=prob[0][2]-prob[0][1]*y
        print("x =",x ,"y =",y)
    elif r ==3:
        
        z=0
        y=0
        x=0
        print("x =",x ,"y =",y,"z =",z)

        
        