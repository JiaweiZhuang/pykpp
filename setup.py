from __future__ import print_function
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(name = 'pykpp',
      version = '1.0rc',
      author = 'Barron Henderson',
      author_email = 'barronh@gmail.com',
      maintainer = 'Barron Henderson',
      maintainer_email = 'barronh@gmail.com',
      url='https://github.com/barronh/pykpp/',
      download_url='https://github.com/barronh/pykpp/archive/master.zip',
      long_description="pykpp is a KPP-like chemical mechanism parser that produces a box model solvable by SciPy's odeint solver",
      packages = ['pykpp', 'pykpp.tuv', 'pykpp.morpho', 'pykpp.models', 'pykpp.test', 'pykpp.funcs'],
      package_dir = {'pykpp': 'src/pykpp'},
      package_data = {'pykpp.models': ['*.eqn', '*.txt', '*.kpp', '*.def']},
      scripts = ['scripts/pykpprun.py'],
      entry_points = {
        'console_scripts': [
            'pykpp = pykpp.__main__:main'
            ]
        },
      install_requires = ['numpy', 'scipy', 'pyparsing']
      )
