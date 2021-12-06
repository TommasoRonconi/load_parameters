# Import data from a parameter file

This is a simple example for showing how to import data saved into a parameter file ([`parameters.py`](parameters.py)) to a script ([`run.py`](run.py)), using command line arguments.

The usage is simply:

```bash
$ python run.py --parm=parameters.py
```

or using `--parm=/path/to/parameters.py` if the parameter file you want to use is in another directory.
