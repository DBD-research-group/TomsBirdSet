from setuptools import find_packages
from setuptools import setup
from birdset import __version__

# def requirements():
#      with open("requirements.txt", "r") as file:
#          lines = file.readlines()
#          lines = [line.rstrip() for line in lines]
#      return lines

setup(
    name='birdset',
    version=__version__,
    description='BirdSet',
    author='Lukas Rauch',
    author_email='lukas.rauch@uni-kassel.de',
    url='https://github.com/DBD-research-group/BirdSet',
    license='BSD 3-Clause',
    packages=find_packages(),
    #install_requires=requirements(),
    extras_require={
    },
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: BSD 3-Clause License',
        'Topic :: Scientific/Engineering :: Artificial Intelligence',
    ],
    keywords='avian monitoring',
    python_requires=">=3.9",
)
