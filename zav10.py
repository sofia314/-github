fromrandomimportrandint 

 

N=int(input()) 

M=int(input()) 

#заповнення матриці довільними значеннями 

A= [ [0]*Mforiinrange(N)] 

foriinrange(N): 

    forjinrange(M): 

        A[i][j] =randint(0,100) 

print(A) 

 

#Визначення середнього значення для всіх рядкув 

foriinrange(N): 

    row_average=0 

    forjinrange(M): 

        row_average+=A[i][j] 

    print('Середне значення по', i+1, 'рядку =', row_average/M) 

 

#Визначення середнього значення для всіх стовпців 

forjinrange(M): 

    column_average=0 

    foriinrange(N): 

        column_average+=A[i][j] 

    print('Середне значення по', j+1, 'стовпцю =',column_average/N) 