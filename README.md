# Nice Figures

A collection of scripts, modules, and style files for making publication quality figures in Matplotlib.

Styles are in accordance with American Physical Society (APS) and Nature publications. 

![alt text](https://github.com/Rob217/nice-figures/blob/master/tests/figs/simple_fig.pdf "Example figure")

To load module:
```python
from nice_figures load *
```

## Functions

The following functions are included:
* [load_style()](./nice_figures/load_style.py)

   Load a set of predefined rcParams.
   
* [add_numbering()](./nice_figures/add_numbering.py)

   Add numbering (e.g., a, b, c, 1, 2, 3, ...) to axes.

* [load_cols()](./nice_figures/load_cols.py)

   Load a dictionary of colors.

* [add_border()](./nice_figures/add_border.py)

   Add a border around the figure. This is useful in, e.g., Jupyter notebooks, where it is unclear how large the figure.

For more details about each function, please see the function docstrings.

## Examples

Example scripts and tests are given in [tests](./tests/).

## Still to do:

* Create separate folder for example scripts
* Add extra example figures showing more complicated behavior
* Specify font sizes for Nature
* Allow indices to go beyond 26 for [add_numbering()](./nice_figures/add_numbering.py)
* Submit to PyPI

## Useful resources

* https://matplotlib.org/3.2.1/tutorials/introductory/customizing.html
* https://journals.aps.org/prl/authors
* https://www.nature.com/nature/for-authors/final-submission

## Where was this package used?

* https://arxiv.org/abs/1907.07030



---
Any suggestions for improvements are very welcome!
