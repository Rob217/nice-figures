print('Testing add_numbering')

from nice_figures import *
import matplotlib.pyplot as plt

fig, ax = plt.subplots()

try: add_numbering(ax, -1)
except ValueError: print('Correctly handled i<0')

try: add_numbering(ax, 26)
except ValueError: print('Correctly handled i>25')

try: add_numbering(ax, numbering='wrong_numbering')
except ValueError: print('Correctly handled incorrect numbering option')

plt.show()

print('Finished testing')
