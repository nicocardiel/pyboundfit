# pyboundfit

Boundary fits using polynomials or splines, based on the method described in
[Cardiel 2009](https://ui.adsabs.harvard.edu/abs/2009MNRAS.396..680C/abstract).
This code is a Python implementation of part of the functionality
implemented in the original Fortran 77 code [boundfit](https://github.com/nicocardiel/boundfit).

## Instaling the code

In order to keep your Python installation clean, it is highly recommended to 
first build a specific Python 3 *virtual enviroment*

### Creating and activating the Python virtual environment

```shell
$ python3 -m venv venv_pyboundfit
$ . venv_pyboundfit/bin/activate
(venv_pyboundfit) $ 
```

### Installing the package

The latest stable version is available via de [PyPI repository](https://pypi.org/project/pyboundfit/):

```shell
(venv_pyboundfit) $ pip install pyboundfit
```
**Note**: This command can also be employed in a Windows terminal opened through the 
``CMD.exe prompt`` icon available in Anaconda Navigator.

The latest development version is available through [GitHub](https://github.com/nicocardiel/pyboundfit):

```shell
(venv_pyboundfit) $ pip install git+https://github.com/nicocardiel/pyboundfit.git@main#egg=pyboundfit
```

### Testing the installation

```shell
(venv_pyboundfit) $ pip show teareduce
```

```shell
(venv_pyboundfit) $ ipython
In [1]: import pyboundfit
In [2]: print(pyboundfit.__version__)
0.1.1
```
