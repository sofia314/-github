Import numpy as np 
from scipy.interpolate import Cubicspline 
import matplotlib. pyplot as plt

x = np. array([e,5, 0.7, 1, 1.4, 1.9])
У = np. array ([2.83, 2.14, 1.46, 1.15, 3.281)
n = 1en(x) - 1
h=np.diff(x)
a=y
b = np. zenos(n)
d = np. zeros(n)
c = np.zeros (n)
alpha = np.zeros (n)
for i in range (1, n);
alpha[i] = (3 / h[i]) * (a[i+1] - a[i]) - (3 / h[i-1]) * (a[i] - a[i-1]):
1 = np.ones(n)
mu = np.zeros(n)
z= np.zeros (n)
for i in range (1, n):
L[i] = 2 * (×[1+1] - x[1-1]) - h[1-1] * mu[i-1]
mu[1] = h[i] / 1[i]
z［i］ =（alpha［2］-h［1-1］*2［1-1］）/ 1［i］

# Виправлення обчислення коефіцієнтів для останнього відрізка
#c[n-1]= 0
c[n-1] = (alpha[n-1] - h[n-2] * =[n-2]) 7 (2 * (h[n-2] + mu[n-1]))
b[n-1] = (a[n] - a[n-1]) / h[n-1] - h[n-1] * (2 * c[n-1] + c[n-2]) / 3
d[n-1] = (c[n-1] - c[n-2]) / (3 * h[n-1])
for j in range(n - 2, -1, -1):
c[S] = 2[3] - mu[f] * c[j+1]
b[i] = (a[j+1] - a[i]) / h[3] - h[i] * (c[j+1] + 2 * c[j]) / 3
d[j] = (c[j+1] - c[j]) / (3 * h[i])
* виведення аналітичного вигляду кубічного сплайна для кожного відрізка
for 1 in range(n):
print(f"відрізок {1+1):")
print(f"S_[1)(x) = (a[i]} + (b[i].round(4)}(x - (x[i])) + (c[i].round(4))(x - {x[i]})^2 + (d[i].round(4))(x - {x[i]})^3,[[×[i] )
# Побудова кубічного сплайна

cs = Cubicspline(x, Y)
# Генерація нових точок для гладкого графіку сплайна
x_new = np. linspace(np.min(X), np. max(x), 100)
_new = cs (x_new)
# Роздрукуйте значення сплайна 
print("Значення (сплайна:")
for i in range(len(x_new)):
print(f"x = {x_new[i]:.2f}, У = (y_new[1]:.3f")
# Побудова графіку
pit:figure(figsize=(8, 6))
pit, plot(x., y, 'o', label='Точки*)
pit.plot(x_new, y_new, Label= кубічний сплайн")
pitaxaabel（'X
pitoyabel（tyny
plt.title("Кубічний сплайн")
pit. Legend () pit.grid(True)
pit. show()