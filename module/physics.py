import math

#Блок 1 - без учета сопротивления воздуха и трения
#===============================================
# Ускорение
def acceleration_noresist(k, m, x):
    ax=-k/m*x   
    return(ax)

# Частота собственных колебаний
def frequency_noresist(k, m):
    omega=math.sqrt(k/m)
    return(omega)

# Период
def period_noresist(k,m):
    T=2*math.pi*math.sqrt(m/k)
    return(T)

# Закон синуса и косинуса:
def sin_noresist(tao, omega, phi, A):
    x=A*math.sin(omega*tao+phi)
    return(x)
def cos_noresist(xm, t, omega, phi):
    x=xm*math.cos(omega*t+phi)
    return(x)

def speed_noresist(omega, xm, A):
    if xm==0:
        vx=omega*A*cos(omega*tao)
    else:
        vx=-omega*A*sin(omega*tao)

# Блок 2 - учет сил сопротивления движению
# ==============================================
# Высчитываем rho - плотность воздуха
def rho_fun(tempC, rt_st, RH, R, Mo, Mh, koef):
    if tempC >= 0:
        E=6.1121*math.exp((17.502*tempC)/(240.97+tempC))
    else:
        E=6.1115*math.exp((22.452*tempC)/(272.55+tempC))
    E=E*100
    e=E*RH/100 # Реальное давление пара
    temp = tempC + 273.15 # Перевод температуры в Кельвины
    p = rt_st*koef # Перевод мм рт. ст. в Па
    rho = ((p-e)*Mo+e*Mh)/(R*temp) # Плотность воздуха
    return(rho)

# Площадь лобового столкновения шара
def s_fun(r):
    S=math.pi*r**2
    return(S)
