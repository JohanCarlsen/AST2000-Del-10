'''
KODESNUT FRA StarPopulation OG EGEN KODE
'''

import numpy as np
import matplotlib.pyplot as plt
from ast2000tools.star_population import StarPopulation
from ast2000tools.solar_system import SolarSystem
import ast2000tools.utils as utils
import ast2000tools.constants as const

stars = StarPopulation()
T = stars.temperatures # [K]
L = stars.luminosities # [L_sun]
r = stars.radii        # [R_sun]

c = stars.colors
s = np.maximum(1e3*(r - r.min())/(r.max() - r.min()), 1.0) # Make point areas proportional to star radii

fig, ax = plt.subplots()
ax.scatter(T, L, c=c, s=s, alpha=0.8, edgecolor='k', linewidth=0.05)

ax.set_xlabel('Temperature [K]')
ax.invert_xaxis()
ax.set_xscale('log')
ax.set_xticks([35000, 18000, 10000, 6000, 4000, 3000])
ax.set_xticklabels(list(map(str, ax.get_xticks())))
ax.set_xlim(40000, 2000)
ax.minorticks_off()

ax.set_ylabel(r'Luminosity [$L_\odot$]')
ax.set_yscale('log')
ax.set_ylim(1e-4, 1e6)

'''
EGEN KODE
'''

'''A'''

# task 1

seed = utils.get_seed('antonabr')
system = SolarSystem(seed)

m_sun = const.m_sun # sun mass in kg
star_temperature = system.star_temperature  # star temperature in Kelvin
star_radius = system.star_radius * 1000    # star radius in m
star_mass_m_sun = system.star_mass  # star mass in m_sun
star_mass_kg = system.star_mass * m_sun    # star mass in kg
sigma = const.sigma # Stefan-Boltzmann constant in W/m^2/K^4
L_sun = const.L_sun # sun luminosity in W

L_star = (4 * np.pi * star_radius**2 * sigma * star_temperature**4) / L_sun  # star luminosity in L_sun, W

# print(f'T_star:\t{star_temperature} K')
# print(f'L_star:\t{L_star*L_sun} W')
# print(f'L_star:\t{L_star} L_sun')
# print(f'L_sun:\t{L_sun} W')
'''
T_star: 7985.019468972192 K
L_star: 3.250701351776308e+27 W
L_star: 8.491905307670606 L_sun
L_sun:  3.828e+26 W
'''

ax.plot(star_temperature, L_star, 'ro', lw=1)


# task 2

seconds_in_year = 60 * 60 * 24 * 365

t_mainsequence_sun = (0.1 * 2 * 1e30 * (3 * 1e8)**2 * 0.007) / (3.7e26) / seconds_in_year

# print(f'{t_mainsequence_sun:e}')
'''
1.079847e+10 ~ 10.8 mrd år
'''

t_life = t_mainsequence_sun / star_mass_m_sun**3    # est time of life on main sequence in years

# print(f'{t_life:e}')
'''
1.444475e+09 ~ 1.5 mrd år
'''


# task 3


'''B'''

# task 1

m_p = const.m_p     # proton mass in kg
m_H = const.m_H2 / 2    # hydrogen mass in kg
m_He = 4 * m_p      # helium mass in kg
k = const.k_B       # Boltzmann constant in m^2*kg/s^2/K
G = const.G     # grav. const in m^3/kg/s^2

GMC_temperature = 10    # K
GMC_mass_m_sun = star_mass_m_sun    # m_sun
GMC_mass_kg = star_mass_kg      # kg

mu = (0.75 * m_H / m_H) + (0.25 * m_He / m_H)   # mean molecular weight in m_H

# print(mu)
'''
1.749341693228085
'''


# task 2

def Jeans_radius(mu, M, T):
    '''Find upper limit to GMC-radius'''

    R = (G * (mu*m_H) * M) / (5 * k * T)

    return R

max_R = Jeans_radius(mu, GMC_mass_kg, GMC_temperature)

# print(f'Radius upper limit: {max_R:e} km')
'''
Radius upper limit: 1.100648e+15 km
'''

GMC_radius = 1e14   # just below max, in km

GMC_lum = (4 * np.pi * (GMC_radius*1000)**2 * sigma * GMC_temperature**4) / L_sun

# print(f'{GMC_lum:e}')
'''
1.861443e+05
'''

# ax.plot(GMC_temperature, GMC_lum, 'ko', lw=1)
ax.set_title('Hertzsprung-Russel diagram')
# plt.savefig('HR_diagram_with_star.png')
# plt.show()
