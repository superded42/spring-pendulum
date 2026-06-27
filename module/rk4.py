# Метод Рунге-Кутты 4-ого порядка
# Вспомогательная  функция. Задаем знак скорости
def sign(vx):
    if vx >0:
        return(1)
    elif vx <0:
        return(-1)
    else:
        return(0)

def rk4f(vx, t, C, rho, S, m, k, x, mu, g, dt, tmas, vxmas, xmas, next_target, last_recorder, mu_s):
    if abs(vx)<1e-9 and k*abs(x)<=mu_s*m*g:
        ax1=0
        vx=0
    else:
        ax1 = -k*x/m-mu*g*sign(vx)-sign(vx)*C*rho*S*vx**2/(2*m)

    k1_vx = ax1 * dt
    k1_x = vx * dt

    vx_mid = vx + 0.5 * k1_vx
    x_mid = x + 0.5 * k1_x

    if abs(vx_mid)<1e-9 and k*abs(x_mid)<=mu_s*m*g:
        ax2=0
        vx_mid=0
    else:
        ax2 = -k*x_mid/m-mu*g*sign(vx_mid)-sign(vx_mid)*C*rho*S*vx_mid**2/(2*m)
    k2_vx = ax2 * dt
    k2_x = vx_mid * dt

    vx_mid = vx + 0.5 * k2_vx
    x_mid = x + 0.5 * k2_x

    if abs(vx_mid)<1e-9 and k*abs(x_mid)<=mu_s*m*g:
        ax3=0
        vx_mid=0
    else:
        ax3 = -k*x_mid/m-mu*g*sign(vx_mid)-sign(vx_mid)*C*rho*S*vx_mid**2/(2*m)
    k3_vx = ax3 * dt
    k3_x = vx_mid * dt

    vx_end = vx + k3_vx
    x_end = x + k3_x

    if abs(vx_end)<1e-9 and k*abs(x_end)<=mu_s*m*g:
        ax4=0
        vx_end=0
    else:
        ax4 = -k*x_end/m-mu*g*sign(vx_end)-sign(vx_end)*C*rho*S*vx_end**2/(2*m)
    k4_vx = ax4 * dt
    k4_x = vx_end * dt

    vx = vx + (k1_vx + 2*k2_vx + 2*k3_vx + k4_vx) / 6
    x = x + (k1_x + 2*k2_x + 2*k3_x + k4_x) / 6
    t = t + dt

    if t>= next_target and next_target > last_recorder:
        last_recorder=t
        next_target=next_target+1.0

        tmas.append(t)
        vxmas.append(vx)
        xmas.append(x)

        print(f'В момент времени {round(t)} с:')
        print(f'Горизонтальная скорость: {vx:.5f}')
        print(f'Абцисса: {x:.5f} м')
        print()


    return{
        'vx':vx,
        'x':x,
        't':t,
        'tmas':tmas,
        'vxmas':vxmas,
        'xmas':xmas,
        'next_target': next_target,
        'last_recorder': last_recorder
    }
