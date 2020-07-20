# Nice Figures

A collection of scripts, modules, and style files for making publication quality figures in Matplotlib.

Styles are in accordance with American Physical Society (APS) and Nature publications. 

![alt text](https://github.com/Rob217/nice-figures/blob/master/examples/figs/advanced_fig.png "Example figure")

To load module:
```python
from nice_figures load *
```

## Installation instructions

This package requires prior intallation of the following packages:
* [numpy](https://numpy.org/install/)

* [matplotlib](https://matplotlib.org/)

I recommend installing for the PyPI server using pip:
```python
pip install nice-figures
```

Alternatively, the files can be downloaded directly from GitHub.

To import, use:
```python
from nice_figures import *
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

Example scripts and figures are given in [examples](./examples/).

## Useful resources

* https://matplotlib.org/3.2.1/tutorials/introductory/customizing.html
* https://journals.aps.org/prl/authors
* https://www.nature.com/nature/for-authors/final-submission

## Where was this package used?

* https://arxiv.org/abs/1907.07030



---
Any suggestions for improvements are very welcome!
