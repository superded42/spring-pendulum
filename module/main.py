import math
import plotext as plt
from physics import acceleration_noresist
from physics import frequency_noresist
from physics import period_noresist
from physics import sin_noresist
from physics import cos_noresist
from rk4 import rk4f
from physics import rho_fun
from physics import s_fun

#==================
#Константы
g = 9.80665
Mo = 28.9644 * 10**(-3)
Mh = 18.0152 * 10**(-3)
R = 8.31446261815324
C = 0.47
koef = 101325 / 760
dt=0.0001
vx=0

#==================

# Симуляция движения пружинного маятника без сопротивления и трения
# ===========================================================
print('Симуляция пружинного маятника')

#Данные
m=float(input('Масса шара в кг: ')or 0.2)
k=float(input('Коэффициент жесткости пружины в Н/м: ') or 30)
phi=float(input('Начальная фаза в рад: ') or 0)
tim=float(input('Время наблюдения эксперимента в с: ') or 20)
xm=float(input('Расстояние от положения равновесия системы в м: ') or -0.05)
print()
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
    if xm == 0:
        x=sin_noresist(xm, tao, omega, phi)
        print('Пока программа не умеет решать при таких данных')
        exit()
    else:
        x=cos_noresist(xm, tao, omega, phi)
    ax=acceleration_noresist(k, m, x)
    
    if tao <= tim:
        times.append(tao)
        X.append(x)
        acc.append(ax)

        print(f'В момент времени {tao:.2f} с: ')
        print(f'Ускорение равно {ax:.2f} м/с^2')
        print(f'Х равен: {x:.2f} м ')
        print()

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
print(f'Период колебаний: {T:.2f} с')
print()


#=================================================================
#То же самое, только с учетом сил сопротивления движения
print('Учет сил сопртивления движению: ')
print('Вводите значения, приближенные к реальности')
print()
mu=float(input('Введите коэффициеет сухого трения (default 0.15): ') or 0.15)
mu_s=1.3*mu #Коэффициент трения покоя(упрощенный)
r=float(input('Введите радиус шара в м: ') or 0.01)
tempC=float(input('Введите температуру воздуха в градусах Цельсия: ') or 22)
rt_st=float(input('Введите атмосферное давление в мм. рт. ст.: ') or 760)
RH=float(input('Введите влажность воздуха в %: ') or 60)

S=s_fun(r)
rho=rho_fun(tempC, rt_st, RH, R, Mo, Mh, koef)

x=float(input('Введите расстояние от точки равновесия системы: ') or -0.05)

t=0
tmas, vxmas, xmas = [], [], []
next_target=0.000000000000000001
last_recorder=0
max_time=20
while (abs(vx) > 1e-9 or k * abs(x) > mu_s * m * g) and t <= max_time:
    data=rk4f(vx, t, C, rho, S, m, k, x, mu, g, dt, tmas, vxmas, xmas, next_target, last_recorder, mu_s)
    
    vx = data['vx']
    x = data['x']
    t = data['t']
    tmas = data['tmas']
    vxmas = data['vxmas']
    xmas = data['xmas']
    next_target = data.get('next_target', next_target)
    last_recorder = data.get('last_recorder', last_recorder)

# График
plt.theme("dark")
plt.plot(data['tmas'], data['xmas'], marker='dot', color='orange')
plt.title("Абцисса")
plt.xlabel("Момент времени")
plt.plotsize(80, 30)
plt.show()
plt.clf()
print()

input('Enter - выйти')
