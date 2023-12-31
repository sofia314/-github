#Метод Крамера 

importnumpyasnp 

 

a=np.matrix('3 -5 3; 1 2 1; 2 7 -1') 

b=np.matrix('1; 4; 8') 

defkram(a,b): 

    det_a=np.linalg.det(a) 

    ifdet_a!=0: 

       a1=np.matrix(a) 

       a2=np.matrix(a) 

       a3=np.matrix(a) 

       a1[:, 0] =b 

       a2[:, 1] =b 

       a3[:, 2] =b 

       x=np.linalg.det(a1)/det_a 

       y=np.linalg.det(a2)/det_a 

       z=np.linalg.det(a3)/det_a 

       print('Solving a system of linear algebraic equations by Cramer*s method') 

       print('x=',x.round(3),'y=',y.round(3),'z=',z.round(3)) 

    else: 

        print('Determinant equals zero, the system has no solutions') 

    returnx,y,z 

kram(a,b) 