# Nice Figures

A collection of scripts, modules, and style files for making publication quality figures in Matplotlib. 

![alt text](https://github.com/Rob217/nice-figures/blob/master/tests/figs/simple_fig.pdf "Example figure")

To load module:
```python
from nice_figures load *
```

## Functions

The following functions are included:
* [load_style()](./nice-figures/load_style.py)

   Load a set of predefined rcParams.
   
* **add_numbering()**

   Add numbering (e.g., a, b, c, 1, 2, 3, ...) to axes.

* **load_cols()**

   Load a dictionary of colors.

* **add_border()**

   Add a border around the figure. This is useful in, e.g., Jupyter notebooks, where it is unclear how large the figure.

For more details about each function, please see the function docstrings.

## Examples
Example scripts and tests are given in [tests](./tests/).

---
Any suggestions for improvements are very welcome!
