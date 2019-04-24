from setuptools import setup

description = (
    "**PEAR** (Petri-net Evolution Analysis Report) is a simple Python program that takes advantage of **Petri nets** and"
    "logical conditions to develop a screening tool aimed at studying the effect of"
    "perturbations in interconnected systems."
)

setup(name='pear',
	  version='0.0.1',
	  description='GRAph Parallel Environment.',
	  long_description=description,
	  url='https://github.com/auroramaurizio/PEAR',
	  author='Aurora Maurizio',
	  author_email='auroramaurizio1@gmail.com',
          keywords='petri-net logical-conditions',
	  license='MIT',
	  packages=['pear'],
	  install_requires=[
	  		'snakes'
	  ],
	  test_suite='nose.collector',
	  tests_require=['nose'],
	  include_package_data=True,
	  zip_safe=False)
