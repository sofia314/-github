

print('A=', a) 

print('B=',b) 

a_inv=np.linalg.inv(a) 

print('A^-1=', a_inv) 

X=a_inv.dot(b) 

print('X=',X) 