from os.path import join, dirname, realpath
from setuptools import setup
import sys

assert sys.version_info.major == 3 and sys.version_info.minor >= 6, \
    "The Spinning Up repo is designed to work with Python 3.6 and greater." \
    + "Please install it before proceeding."

with open(join("spinup", "version.py")) as version_file:
    exec(version_file.read())

setup(
    name='spinup',
    py_modules=['spinup'],
    version=__version__,#'0.1',
    install_requires=[
        'cloudpickle==1.2.1',
        'gym[atari,box2d,classic_control]~=0.15.7',
        'pyglet==1.5.15',
        'PyOpenGL==3.1.7',
        'ipython==8.19.0',
        'joblib',
        'matplotlib==3.1.1',
        'mpi4py==3.1.5',
        'numpy==1.23.5',
        'pandas==1.5.3',
        'pytest',
        'psutil',
        'scipy==1.10.1',
        'seaborn==0.8.1',
        # 'tensorflow>=1.8.0,<2.0',
        # 'torch==1.3.1',
        'tqdm'
    ],
    description="Teaching tools for introducing people to deep RL.",
    author="Joshua Achiam",
)
