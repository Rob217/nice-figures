# import numpy as np
# import matplotlib.pyplot as plt
import matplotlib as mpl
from cycler import cycler
from .load_cols import load_cols

def load_style(style='APS', width='1-column'):
  """
  Set custom matplotlib.rcParams.

  This sets the rcParams for a range of different options.
  For a list of all possible rcParams see
  https://matplotlib.org/3.2.1/tutorials/introductory/customizing.html

  To add/modify rcParams simply add the following line to the figure script:
  mpl.rcParams.update({'rcParam_key' : 'rcParam_value'})

  This package currently provides default values for two styles:
    - APS (American Physical Society)
      https://journals.aps.org/prl/authors
    - Nature
      https://www.nature.com/nature/for-authors/final-submission

  Paramaters:
  -----------
  style : string
    'APS' or 'Nature'
  width : string
    Figure width in columns
    '1-column', '1.5-column', '2-column'

  Returns:
  --------
  figsize : dict of tuples
    keys -> (style, width)
    values -> (fig_width, fig_height)
    Note that fig_width and fig_height are in inches by default.
  """

  if style not in ('APS', 'Nature'):
    raise ValueError("style must be 'APS' or 'Nature'")
  if width not in ('1-column', '1.5-column', '2-column'):
    raise ValueError("width must be '1-column', '1.5-column', or '2-column'")

  # reset default parameters
  mpl.rcParams.update(mpl.rcParamsDefault)

  figsize = {('APS', '1-column') : (3.375, 3),
             ('APS', '1.5-column') : (5.0625, 3),
             ('APS', '2-column') : (6.75, 3),
             ('Nature', '1-column') : (3.50394, 3),
             ('Nature', '1.5-column') : (5.35, 3),
             ('Nature', '2-column') : (7.204724, 3),
  }

  cols = load_cols()

  params = {
    'text.usetex' : True, # use latex text
    'text.latex.preamble' : r'\usepackage{braket}\usepackage{amssymb}\usepackage{txfonts}', # latex packages
    'font.family' : r'Times New Roman',
    'figure.dpi' : 300,
    'figure.figsize' : figsize[(style, width)],
    'figure.autolayout' : True, # tight layout (True) or not (False)
    'axes.labelpad' : 1,
    'axes.xmargin' : 0,
    'axes.ymargin' : 0,
    # 'axes.autolimit_mode' : round_numbers, # set axis limits by rounding min/max values
    'axes.autolimit_mode' : 'data', # set axis limits as min/max values
    'xtick.major.pad' : 2,
    'ytick.major.pad' : 2,
    'lines.linewidth' : 1.3,
    'xtick.direction' : 'in',
    'ytick.direction' : 'in',
    'xtick.top' : True,
    'ytick.right' : True,
    'xtick.minor.visible' : True,
    'ytick.minor.visible' : True,
    'axes.prop_cycle': cycler(color = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b', '#e377c2', '#7f7f7f', '#bcbd22', '#17becf']*3, ls = ['-', '--', '-.']*10),
    'legend.framealpha': None
  }

  mpl.rcParams.update(params)

  return figsize
