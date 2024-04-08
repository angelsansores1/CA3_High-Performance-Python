from distutils.core import setup
from Cython.Build import cythonize

setup(
    ext_modules = cythonize(["Cython1.pyx", "Cython2.pyx", "Cython3.pyx", "Cython4.pyx"])
)