import math
import plotext as plt
from physics import acceleration_noresist
from physics import frequency_noresist
from physics import period_noresist
from physics import sin_noresist
from physics import cos_noresist
from rk4 import rk4f

#==================
g=9.8
C=0.47
S=0.7
dt=0.0001
vx=0
mu=0.01
rho=1
x=1
#==================

# Симуляция движения пружинного маятника без сопротивления и трения
# ===========================================================
print('Симуляция пружинного маятника')

#Данные
m=float(input('Масса шара в кг: ')or 4)
k=float(input('Коэффициент жесткости пружины в Н/м: ') or 1)
phi=float(input('Начальная фаза в рад: ') or 0)
tim=float(input('Время наблюдения эксперимента в с: ') or 200)
xm=float(input('Амплитуда: ') or 0.05)
if m == 0 or k == 0:
    print('Неверные значения')
    exit()

#Массивы
times = []
X=[]
acc=[]
steps=100

# tao - момент времени
omega=frequency_noresist(k, m)
T=period_noresist(k, m)

#Вычислительный процесс
for i in range (steps + 1):
    tao=tim*i/steps
    x=sin_noresist(xm, tao, omega, phi)
    ax=acceleration_noresist(k, m, x)
    
    if tao <= tim:
        times.append(tao)
        X.append(x)
        acc.append(ax)

        print(f'В момент времени {tao:.2f} с: ')
        print(f'Ускорение равно {ax:.2f} м/с^2')
        print(f'Х равен: {x:.2f} м ')
        print()

print(f'Период колебаний: {T:.2f} с')
# График
plt.theme("dark")
plt.plot(times, X, marker='dot', color='orange')
plt.title("X")
plt.xlabel("tao")
plt.plotsize(80, 30)
plt.show()
plt.clf()
print()


plt.theme("dark")
plt.plot(times, acc, marker='dot', color='orange')
plt.title("Ускорение")
plt.xlabel("tao")
plt.plotsize(80, 30)
plt.show()
plt.clf()
print()

#=================================================================
#То же самое, только с учетом сил сопротивления движения
print('Данные с учетом сил сопротивления: ')
t=0
tmas, vxmas, xmas = [], [], []
next_target=0.0000000000000000000000001
last_recorder=0
while abs(vx) > 1e-10 or abs(x) > 1e-10:
    data=rk4f(vx, t, C, rho, S, m, k, x, mu, g, dt, tmas, vxmas, xmas, next_target, last_recorder)
    vx = data['vx']
    x = data['x']
    t = data['t']
    tmas = data['tmas']
    vxmas = data['vxmas']
    xmas = data['xmas']
    next_target = data.get('next_target', next_target)
    last_recorder = data.get('last_recorder', last_recorder)
plt.theme("dark")
plt.plot(data['tmas'], data['xmas'], marker='dot', color='orange')
plt.title("Абцисса")
plt.xlabel("Момент времени")
plt.plotsize(80, 30)
plt.show()
plt.clf()
print()

input('Enter - выйти')
