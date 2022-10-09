from setuptools import setup
import os

file_dir = os.path.abspath(os.path.dirname(__file__))
os.chdir(file_dir)

setup(name="union_like",
      version='1.0',
      description='SNe Union external Cobaya likelihood package',
      zip_safe=True,  
      packages=['union_like'],
      package_data={'union_like': ['*.yaml', 'union_data/*']},
      install_requires=['cobaya (>=2.0.5)'],
      )
