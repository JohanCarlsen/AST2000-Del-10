'''
EGEN KODE
'''

'''B'''


import numpy as np
import matplotlib.pyplot as plt
from ast2000tools.star_population import StarPopulation
from ast2000tools.solar_system import SolarSystem
import ast2000tools.utils as utils
import ast2000tools.constants as const
import scipy.constants as constant

seed = utils.get_seed('antonabr')
system = SolarSystem(seed)

m_sun = const.m_sun     # kg
m_H = const.m_H2 / 2    # hydrogen mass in kg
m_e = constant.m_e      # kg
h = constant.h          # J Hz^-1
G = const.G             # m^3/kg/s^2

star_mass = system.star_mass * m_sun    # kg
M_Ch = 1.4 * m_sun                      # kg

M_WD = (star_mass / (8 * m_sun)) * M_Ch   # kg

# print(f'White drarf mass: {M_WD:.3e} kg')
'''
White dwarf mass: 6.804e+29 kg
'''

R_WD = ((3 / (2*np.pi))**(4/3) * (h**2 / (20 * m_e * G)) * (1 / (2 * m_H))**(5/3) * M_WD**(-1/3)) / 1000    # km

# print(f'White dwarf radius: {R_WD:.3f} km')
'''
White dwarf radius: 2045.162 km
'''

rho_WD = M_WD / ((4/3) * np.pi * (R_WD*1000)**3)    # kg/m^3

# print(f' White dwarf density: {rho_WD:.3e} kg/m^3')
'''
 White dwarf density: 1.899e+10 kg/m^3
'''

# print(f'One liter of white dwarf weighs: {rho_WD*1e-3:.3e} kg')
'''
One liter of white dwarf weighs: 1.899e+07 kg
'''

grav_acc = G * M_WD / (R_WD*1000)**2
earth_grav_acc = G * 5.972e24 / 6371e3**2

# print(f'Gravitational acceleration on drawf star:\t{grav_acc:.3e} m/s^2')
# print(f'Gravitational acceleration on earth:\t\t{earth_grav_acc:.3f} m/s^2')
# print(f'g is {grav_acc/earth_grav_acc:.2e} times greater on WD.')
'''
Gravitational acceleration on drawf star:       1.086e+07 m/s^2
Gravitational acceleration on earth:            9.820 m/s^2
g is 1.11e+06 times greater on WD.
'''
