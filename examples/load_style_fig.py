"""
Generating example figures for different available styles in load_style()
"""

import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import os
from nice_figures import *

styles = ('APS', 'Nature')
widths = ('1-column', '1.5-column', '2-column')

x = np.linspace(0, 4*np.pi, 101)
y = np.sin(x)

for style in styles:
  for width in widths:

    load_style(style, width)
    fig, ax = plt.subplots()
    ax.plot(x, y)
    ax.set_ylabel(r'$y$')
    ax.set_xlabel(r'$x$')
    ax.set_title(style + ', ' + width)
    plt.savefig(os.path.join('figs', \
                'load_style_' + style + '_' + width + '.png'))

# custom height
figsize = load_style()
w, h = figsize[('APS', '1-column')]
fig, ax = plt.subplots(figsize=(w, 6))
ax.plot(x, y)
ax.set_ylabel(r'$y$')
ax.set_xlabel(r'$x$')
ax.set_title('Width = APS, 1-column; Height = 6in')
plt.savefig(os.path.join('figs', \
            'load_style_APS_1-column_h=6in.png'))

# custom width + height
figsize = load_style()
fig, ax = plt.subplots(figsize=(2, 5))
ax.plot(x, y)
ax.set_ylabel(r'$y$')
ax.set_xlabel(r'$x$')
ax.set_title('Width = 2in; Height = 5in')
plt.savefig(os.path.join('figs', \
            'load_style_w=2in_h=5in.png'))
plt.show()
