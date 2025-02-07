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
```
```python
In [1]: import pyboundfit

In [2]: print(pyboundfit.__version__)
0.2.0

In [3]: pol1, pol2, spl1, spl2 = pyboundfit.demo()
Computing upper boundary (polynomial fit)... OK!
Computing lower boundary (polynomial fit)... OK!
Computing upper boundary (splines fit)... OK!
Computing lower boundary (splines fit)... OK!

In [4]: pol1.coef
Out[4]: 
array([  23.93468048,  -27.52145834,   10.30357372,   84.12092668,
         24.85352908, -107.79404231])
...
```

The demo function computes the boundary fits to some example data and
generates the following plot:
![pyboundfit demo plot](https://guaix.fis.ucm.es/~ncl/pyboundfit/pyboundfit_example.png)
