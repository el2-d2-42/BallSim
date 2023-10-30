from setuptools import setup 

setup( 
	name='BallSim', 
	version='0.1', 
	description='''This repository contains a Python 
 		program that simulates a plate tasked with balancing 
   		a ball on its surface.''', 
	author='Emanuel Peruzzi', 
	author_email='eperuzzi@icloud.com', 
	packages=['BallSim'], 
	install_requires=[ 
		'numpy', 
		'pandas',
		'pygame',
	], 
) 
