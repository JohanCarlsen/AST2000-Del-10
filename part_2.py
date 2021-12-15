'''
EGEN KODE
'''

'''A'''


import numpy as np
import matplotlib.pyplot as plt
from ast2000tools.star_population import StarPopulation
from ast2000tools.solar_system import SolarSystem
import ast2000tools.utils as utils
import ast2000tools.constants as const

seed = utils.get_seed('antonabr')
system = SolarSystem(seed)

m_sun = const.m_sun     # kg
k = const.k_B           # Boltzmann constant in m^2*kg/s^2/K
G = const.G             # grav. const in m^3/kg/s^2
m_p = const.m_p         # proton mass in kg
m_H = const.m_H2 / 2    # hydrogen mass in kg
m_He = 4 * m_p          # helium mass in kg
sigma = const.sigma     # Stefan-Boltzmann constant in W/m^2/K^4

star_temperature = system.star_temperature              # K
star_mass = system.star_mass * m_sun                    # kg
star_radius = system.star_radius * 1000                 # m
rho_0 = star_mass / ((4/3) * np.pi * star_radius**3)
mu = (0.75 * m_H / m_H) + (0.25 * m_He / m_H)           # mean molecular weight in m_H

T_core = star_temperature + ((2*np.pi/3) * G * rho_0 * (m_H/k) * star_radius**2) # K

sun_T_core = 15e6           # K
sun_radius = 396340         # km
sun_temperature = 57778     # K

# print('\tMass [kg]\tRadius [km]\tT_surf [K]\tT_c [K]')
# print(f'Star\t{star_mass:.2e}\t{star_radius:.2e}\t{star_temperature:.2e}\t{T_core:.2e}')
# print(f'Sun\t{m_sun:.2e}\t{sun_radius:.2e}\t{sun_temperature:.2e}\t{sun_T_core:.2e}')
# print('')
# print('Relations:')
# print(f'Star mass:\t{star_mass/m_sun:.2f} m_sun')
# print(f'Star radius:\t{star_radius/sun_radius:.2f} r_sun')
# print(f'Star T_surf:\t{star_temperature/sun_temperature:.2f} T_sun')
# print(f'Star T_c:\t{T_core/sun_T_core:.2f} T_c_sun')
'''
        Mass [kg]       Radius [km]     T_surf [K]      T_c [K]
Star    3.89e+30        1.06e+09        7.99e+03        1.49e+07
Sun     1.99e+30        3.96e+05        5.78e+04        1.50e+07

Relations:
Star mass:      1.96 m_sun
Star radius:    2672.75 r_sun
Star T_surf:    0.14 T_sun
Star T_c:       0.99 T_c_sun
'''

# print(f'{T_core:e}')
'''
1.485667e+07
'''

'''B'''

X_H = 0.745
X_CNO = 0.002

e_0_pp = 1.08e-12   # Wm^3/kg^2
e_0_CNO = 8.24e-31  # Wm^3/kg^2

T_6 = T_core / 1e6

e_pp = e_0_pp * X_H**2 * rho_0 * T_6**4             # pp-chain
e_CNO = e_0_CNO * X_H * X_CNO * rho_0 * T_6**20     # CNO-cycle

# print(f'e_pp:\t{e_pp:.3e} W/kg')
# print(f'e_CNO:\t{e_CNO:.3e} W/kg')
'''
e_pp:   2.280e-05 W/kg
e_CNO:  2.631e-07 W/kg
'''
L_star =  3.250701351776308e+27                                     # from last part in W
Lum = (4*np.pi/3) * rho_0 * (e_pp + e_CNO) * (0.2 * star_radius)**3 # W

# print(f'Old luminosity: {L_star:.3e} W')
# print(f'New luminosity: {Lum:.3e} W')
# print(f'Relative error: {abs(L_star-Lum)/L_star:.5f}, in percent: {(abs(L_star-Lum)/L_star)*100:.3f} %')
'''
Old luminosity: 3.251e+27 W
New luminosity: 7.175e+23 W
Relative error: 0.99978, in percent: 99.978 %
'''

Temp = (Lum / (4 * np.pi * star_radius**2 * sigma))**(1/4)

# print(f'Old temperature: {star_temperature:.2f} K')
# print(f'New temperature: {Temp:.2f} K')
# print(f'Relative error: {abs(star_temperature-Temp)/star_temperature:.5f}, in percent: {(abs(star_temperature-Temp)/star_temperature)*100:.3f} %')
'''
Old temperature: 7985.02 K
New temperature: 973.27 K
Relative error: 0.87811, in percent: 87.811 %
'''
