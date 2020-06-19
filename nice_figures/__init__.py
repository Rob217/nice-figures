from .version import __version__
from .add_numbering import add_numbering
from .load_style import load_style
from .add_border import add_border
from .load_cols import load_cols

# if somebody does "from nice_figures import *", this is what they will
# be able to access:
__all__ = [
    'add_numbering',
    'load_style',
    'add_border',
    'load_cols',
]
