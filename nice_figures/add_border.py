import matplotlib.pyplot as plt

def add_border():
  """
  Add red border to figure.

  Helps to see how large figure extent is when using, e.g., Jupyter notebook.
  """

  ax = plt.axes([0,0,1,1], facecolor=(1,1,1,0))
  ax.tick_params(axis='both', which='both', labelbottom=False, labelleft=False, length=0)
  [spine.set_color('r') for dummy, spine in ax.spines.items()]

  pass
