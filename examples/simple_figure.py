'''
A simple single-panel figure template
'''

import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import os
from nice_figures import *

load_style()

fig, axs = plt.subplots()
x = np.linspace(0, 6*np.pi, 201)
axs.plot(x, np.sin(x), label=r'$\sin(x)$')
axs.plot(x, np.cos(x), label=r'$\cos(x)$')
axs.plot(x, np.cos(x)**2, label=r'$\cos^2(x)$')
axs.set_xlabel(r'$x$')
axs.set_ylabel(r'$f(x)$')
axs.legend(loc=3)

plt.savefig(os.path.join('figs', 'simple_fig.png'))
plt.show()
