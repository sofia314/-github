#Підрозділ 5 

h=np.matrix('1 2 0 0 0; 1 0 2 0 0; 1 0 0 2 0; 1 0 0 0 2; 0 0 1 1 1')#Задаємо матрицю 

h_det=np.linalg.det(h) #Визначник матриці 

print(format(h_det, '.9g')) 