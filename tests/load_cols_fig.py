
"""
Loading and plotting colors from cols.json using load_cols()
"""

import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import os
from nice_figures import *

cols = load_cols()
load_style()

fig, ax = plt.subplots()
for i_col, col in enumerate(cols):
  ax.axhline(len(cols) - i_col, color=cols[col], lw=2, label=col)
ax.set_ylim([0, len(cols)+1])
ax.legend()

plt.savefig(os.path.join('figs', 'load_cols_fig.pdf'))
plt.show()
