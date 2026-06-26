# Метод Рунге-Кутты 4-ого порядка
def rk4f(vx, t, C, rho, S, m, k, x, mu, g, dt, tmas, vxmas, xmas, next_target, last_recorder):
    ax1 = -k*x/m+mu*g*x-C*rho*S*vx**2/(2*m)

    k1_vx = ax1 * dt
    k1_x = vx * dt

    vx_mid = vx + 0.5 * k1_vx
    x_mid = x + 0.5 * k1_x

    vx2 = vx_mid 
    ax2 = -k*x_mid/m+mu*g*x_mid-C*rho*S*vx2**2/(2*m)

    k2_vx = ax2 * dt
    k2_x = vx_mid * dt

    vx_mid = vx + 0.5 * k2_vx
    x_mid = x + 0.5 * k2_x

    vx3 = vx_mid 
    ax3 = -k*x_mid/m+mu*g*x_mid-C*rho*S*vx3**2/(2*m)

    k3_vx = ax3 * dt
    k3_x = vx_mid * dt

    vx_end = vx + k3_vx
    x_end = x + k3_x

    vx4 = vx_end 
    ax4 = -k*x_mid/m+mu*g*x_mid-C*rho*S*vx4**2/(2*m)

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

        print('В момент времени {t:.2f} с:')
        print('Горизонтальная скорость: {vx:.2f}')
        print('Абцисса: {x:.2f} м')


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
