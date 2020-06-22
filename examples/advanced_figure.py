'''
An example figure with a colormap and cross-sections
'''

# load modules
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import os
from nice_figures import *

figsizes = load_style()
mpl.rcParams.update({'figure.autolayout' : False}) # cannot use tight layout with custom axis positions

# create data
x = np.linspace(-4, 4, 201)
y = np.linspace(-4, 4, 203)
X, Y = np.meshgrid(x, y)
Z = np.exp(-((X-1)**2 + (Y+2)**2)/3) + np.exp(-((X+1.5)**2 + (Y-1)**2)/1)
z_label = r'$f(x,y)$'

# initialize figure
fig_w, fig_h = figsizes[('APS', '1-column')]
fig = plt.figure(figsize = (fig_w, 1.1*fig_w))
axs = {}

# initialize axes manually
ax_x, ax_y, ax_w, ax_h = (0.11, 0.31, 0.65, 0.55)
ax_t, ax_gap = (0.2, 0.03)
axs['main'] = plt.axes([ax_x, ax_y, ax_w, ax_h])
axs['right'] = plt.axes([ax_x + ax_w + ax_gap, ax_y, ax_t, ax_h])
axs['bottom'] = plt.axes([ax_x, ax_y - ax_gap - ax_t, ax_w, ax_t])
axs['cb'] = plt.axes([ax_x, ax_y + ax_h + 0.01, ax_w, 0.04])

# remove tick labels
axs['main'].axes.xaxis.set_ticklabels([])
axs['right'].axes.yaxis.set_ticklabels([])
axs['cb'].axes.yaxis.set_ticks([])
axs['cb'].tick_params(labelbottom=False, labeltop=True)

# plot data
clims = (0, 1)
image = axs['main'].imshow(Z, extent=[x[0], x[-1], y[0], y[-1]], vmax=clims[1], vmin=clims[0], aspect='auto')
axs['right'].plot(np.flipud(np.max(Z, axis=1)), y)
axs['bottom'].plot(x, np.max(Z, axis=0))

# add colorbar
cb = fig.colorbar(image, cax=axs['cb'], orientation='horizontal')
cb.ax.tick_params(labelbottom=False, labeltop=True, which='both', top=True)
cb.ax.set_xlabel(z_label, labelpad=4)
cb.ax.xaxis.set_label_position('top')

# add axis labels and set limits
axs['main'].set_ylabel(r'$y$')
axs['right'].set_xlabel(z_label)
axs['bottom'].set_xlabel(r'$x$')
axs['bottom'].set_ylabel(z_label)
axs['right'].set_xlim(clims)
axs['bottom'].set_ylim(clims)

# add axis numbering
add_numbering(axs['main'], i=0, loc=(0.9, 0.9), **{'color' : 'w'})
add_numbering(axs['right'], i=1, loc=(0.7, 0.9))
add_numbering(axs['bottom'], i=2, loc=(0.9, 0.8))

# save
plt.savefig(os.path.join('figs', 'advanced_fig.png'))

plt.show()
