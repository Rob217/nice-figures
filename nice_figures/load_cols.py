import json
import os
from pkg_resources import resource_stream

def load_cols():
  """
  Load dictionary of colors from /data/cols.json

  For the moment, these colors are just the default color cycle for
  Matplotlib 2.0. However, in future more colors may be added to this.

  Returns:
  --------
  cols : dict
    keys -> color names
    values -> color hex values
  """

  filename = os.path.join('data', 'cols.json')
  json_string = resource_stream(__name__, filename).read().decode()
  cols = json.loads(json_string)

  # f = open(os.path.join('data', 'cols.json'))
  # cols = json.load(f)
  # f.close()

  return cols

if __name__=="__main__":
  print(load_cols())
