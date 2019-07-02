from setuptools import setup, find_packages
from os import path

here = path.abspath(path.dirname(__file__))
with open(path.join(here, 'README.md')) as f:
    long_description = f.read()

setup(
    name='pyDICI',
    version='0.0.4',
    packages=find_packages(),
    url='https://github.com/danielsioli/DICI',
    author='Daniel Oliveira',
    author_email='danielsioli@gmail.com',
    license='Creative Commons Attribution-Noncommercial-Share Alike license',
    description='Pacote para enviar dados ao DICI',
    long_description=long_description,
    long_description_content_type="text/markdown",
    keywords='anatel,dici',
    install_requires=['selenium','datetime','argparse','pandas','termcolor','xlrd'],
    include_package_data=True,
    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 4 - Beta',

        # Indicate who your project is intended for
        'Intended Audience :: Developers',
        'Topic :: Internet :: WWW/HTTP',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ]
)
