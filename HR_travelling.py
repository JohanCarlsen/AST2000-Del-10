import numpy as np
import matplotlib.pyplot as plt
from ast2000tools.star_population import StarPopulation
from ast2000tools.solar_system import SolarSystem
import ast2000tools.utils as utils
import ast2000tools.constants as const

seed = utils.get_seed('antonabr')
system = SolarSystem(seed)

r_sun = 396340
R = system.star_radius / r_sun

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
ax.set_title('Hertzsprung-Russel diagram')

T_star = 7985.019468972192   # K
L_star = 8.491905307670606   # L_sun

ax.scatter(6000, 10**5, s=16*16, color='red')
ax.scatter(12000, 10**4.5, s=8*16, color='red')
ax.scatter(18000, 10**4.25, s=3*16, color='red')
ax.scatter(24000, 10**4, s=16, color='red')
ax.scatter(20000, 1e-2, s=8, color='blue')
plt.savefig('HR-travel-5.png')

# plt.show()
