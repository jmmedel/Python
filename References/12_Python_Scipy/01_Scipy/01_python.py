

"""
SciPy Tutorial


SciPy, a scientific library for Python is an open source, BSD-licensed library for mathematics, science and engineering. The SciPy library depends on NumPy, which provides convenient and fast N-dimensional array manipulation. The main reason for building the SciPy library is that, it should work with NumPy arrays. It provides many user-friendly and efficient numerical practices such as routines for numerical integration and optimization. This is an introductory tutorial, which covers the fundamentals of SciPy and describes how to deal with its various modules.

Audience
This tutorial is prepared for the readers, who want to learn the basic features along with the various functions of SciPy. After completing this tutorial, the readers will find themselves at a moderate level of expertise, from where they can take themselves to higher levels of expertise.

Prerequisites
Before proceeding with the various concepts given in this tutorial, it is being expected that the readers have a basic understanding of Python. In addition to this, it will be very helpful, if the readers have some basic knowledge of other programming languages. SciPy library depends on the NumPy library, hence learning the basics of NumPy makes the understanding easy.

SciPy - Introduction
SciPy, pronounced as Sigh Pi, is a scientific python open source, distributed under the BSD licensed library to perform Mathematical, Scientific and Engineering Computations.

The SciPy library depends on NumPy, which provides convenient and fast N-dimensional array manipulation. The SciPy library is built to work with NumPy arrays and provides many user-friendly and efficient numerical practices such as routines for numerical integration and optimization. Together, they run on all popular operating systems, are quick to install and are free of charge. NumPy and SciPy are easy to use, but powerful enough to depend on by some of the world's leading scientists and engineers.

SciPy Sub-packages
SciPy is organized into sub-packages covering different scientific computing domains. These are summarized in the following table −

scipy.cluster	Vector quantization / Kmeans
scipy.constants	Physical and mathematical constants
scipy.fftpack	Fourier transform
scipy.integrate	Integration routines
scipy.interpolate	Interpolation
scipy.io	Data input and output
scipy.linalg	Linear algebra routines
scipy.ndimage	n-dimensional image package
scipy.odr	Orthogonal distance regression
scipy.optimize	Optimization
scipy.signal	Signal processing
scipy.sparse	Sparse matrices
scipy.spatial	Spatial data structures and algorithms
scipy.special	Any special mathematical functions
scipy.stats	Statistics
Data Structure
The basic data structure used by SciPy is a multidimensional array provided by the NumPy module. NumPy provides some functions for Linear Algebra, Fourier Transforms and Random Number Generation, but not with the generality of the equivalent functions in SciPy.


Standard Python distribution does not come bundled with any SciPy module. A lightweight alternative is to install SciPy using the popular Python package installer,

pip install pandas
If we install the Anaconda Python package, Pandas will be installed by default. Following are the packages and links to install them in different operating systems.

Windows
Anaconda (from https://www.continuum.io) is a free Python distribution for the SciPy stack. It is also available for Linux and Mac.

Canopy (https://www.enthought.com/products/canopy/) is available free, as well as for commercial distribution with a full SciPy stack for Windows, Linux and Mac.

Python (x,y) − It is a free Python distribution with SciPy stack and Spyder IDE for Windows OS. (Downloadable from https://python-xy.github.io/)

Linux
Package managers of respective Linux distributions are used to install one or more packages in the SciPy stack.

Ubuntu
We can use the following path to install Python in Ubuntu.

sudo apt-get install python-numpy python-scipy 
python-matplotlibipythonipython-notebook python-pandas python-sympy python-nose
Fedora
We can use the following path to install Python in Fedora.

sudo yum install numpyscipy python-matplotlibipython python-pandas 
sympy python-nose atlas-devel

"""
