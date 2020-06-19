print('Testing load_style()')

from nice_figures import *

try: load_style(style='wrong_style')
except ValueError: print('Correctly handled incorrect style')

try: load_style(width='wrong_width')
except ValueError: print('Correctly handled incorrect width')

print('Finished testing')
