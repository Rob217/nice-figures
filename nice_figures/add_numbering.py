import string

def add_numbering(ax, i=0, loc=(0.8, 0.8), label='', style='APS', numbering='abc', **kwargs):
  """
  Add numbering (a,b,c,...) to axis.

  Parameters
  ----------
  ax : matplotlib.pyplot.axis object
  i : int
    The axis index, e.g., i=1 -> (a)
  loc : tuple or list
    Position of label, relative to axis
    [x, y] where 0 <= x,y <= 1
    (values outside this limit are allowed but may result in labels outside axis)
  label : string
    Override with custom label
  style : string
    If 'APS' or 'Nature' will use preset styles
    Otherwise if string matches format r'{i}' will use that as template string
    Otherwise style overwrites the label
  numbering : string
    Which type of numbering
    'abc' -> a, b, c
    'ABC' -> A, B, C
    '123' -> 1, 2, 3
    'roman' -> i, ii, iii
    'ROMAN' -> I, II, III

  **kwargs : string keyword arguments
    e.g. {'color', 'red'}

  Returns
  -------
  ax : matplotlib.pyplot.axis object
  """

  if not label:

    if i<0 or i>25:
      raise ValueError("i must be between 0 and 25 \
                        (support for i>25 will come in future version)")

    roman_nums = ['i', 'ii', 'iii', 'iv', 'v', 'vi', 'vii', 'viii', 'ix', 'x',\
                  'xi', 'xii', 'xiii', 'xiv', 'xv', 'xvi', 'xvii', 'xviii', \
                  'xix', 'xx', 'xxi', 'xxii', 'xxiii', 'xxiv', 'xxv', 'xxvi']

    # different formats:
    if numbering == 'abc': # a, b, c
      label = string.ascii_lowercase[i]
    elif numbering == 'ABC': # A, B, C
      label = string.ascii_uppercase[i]
    elif numbering == '123': # 1, 2, 3
      label = i
    elif numbering == 'roman': # i, ii, iii, ...
      label = r'${}$'.format(roman_nums[i])
    elif numbering == 'ROMAN': # I, II, III, ...
      label = r'{}'.format(roman_nums[i].upper())
    else:
      raise ValueError("numbering option not a recognized value")

    if style == 'APS':
      label = r'({})'.format(label)
    elif style == 'Nature':
      label = r'\textbf{{{i}}}'.format(i=label)
    else:
      label = style.format(i=label)


  ax.text(loc[0], loc[1], label, transform=ax.transAxes, **kwargs)

  return ax
