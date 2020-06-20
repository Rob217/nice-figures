
'''
Figures showing the different configurations for add_numbering()
'''

import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import os
from nice_figures import *

load_style()

fig, axs = plt.subplots(4, 2, figsize=(3, 4))

for ax in axs.flatten():
  ax.tick_params(axis='both', which='both', left=False, right=False, top=False, bottom=False, labelbottom=False, labelleft=False)

locs = ((0.1, 0.1), (0.4, 0.5), (0.7, 0.8))

for i in range(3):

  axs[0, 0].set_title('default (APS, abc)')
  add_numbering(axs[0, 0], i, loc=locs[i])

  axs[0, 1].set_title('style=Nature')
  add_numbering(axs[0, 1], i, loc=locs[i], style='Nature')

  axs[1, 0].set_title('custom style + **kwargs')
  add_numbering(axs[1, 0], i, loc=locs[i], style=r'[\textit{{{i}}}]', **{'color':'red'})

  axs[1, 1].set_title('custom label')
  custom_labels = [r'$\alpha$', r'$\beta$', r'$\gamma$']
  add_numbering(axs[1, 1], i, loc=locs[i], label=custom_labels[i])

  axs[2, 0].set_title('ABC')
  add_numbering(axs[2, 0], i, loc=locs[i], numbering='ABC')

  axs[2, 1].set_title('123')
  add_numbering(axs[2, 1], i, loc=locs[i], numbering='123')

  axs[3, 0].set_title('roman')
  add_numbering(axs[3, 0], i, loc=locs[i], numbering='roman')

  axs[3, 1].set_title('ROMAN')
  add_numbering(axs[3, 1], i, loc=locs[i], numbering='ROMAN')

plt.savefig(os.path.join('figs', 'add_numbering_fig.png'))
plt.show()
