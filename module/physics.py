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
def sin_noresist(xm, tao, omega, phi):
    x=math.sin(omega*tao+phi)
    return(x)
def cos_noresist(xm, t, omega, phi):
    x=math.cos(omega*t+phi)
    return(x)

