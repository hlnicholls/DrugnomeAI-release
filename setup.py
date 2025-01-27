from setuptools import setup, find_packages 
import io

setup(	name='Drugnome-AI',
	version='1.0.0',
	author='Arwa Raies, James Stainer, Ewa Tulodziecka, Dimitrios Vitsios',
	author_email='dimitrios.vitsios@astrazeneca.com',
	description='DrugnomeAI: Target Druggability Prediction from Public Data by Stochastic Semi-Supervised Learning',
	url="https://github.com/AstraZeneca-CGR/drugnomeAI",
	packages=find_packages(),
	python_requires='>=3.6',
	install_requires=['setuptools==39.1.0',
			  'numpy==1.16.3',
			  'numpydoc==0.8.0',
			  'pandas==0.24.2',
 			  'scipy==1.2.1',
			  'scikit-learn==0.20.3',
		    	  'bokeh==1.1.0',
			  'h5py==2.9.0',
			  'tensorflow==1.12.0',
			  'Keras==2.2.4',
			  'matplotlib==3.0.3',
			  'palettable==3.1.1',
			  'plotly==3.9.0',
			  'PyYAML==5.1',
			  'seaborn==0.9.0',
			  'tables==3.5.1',
			  'twine==3.0.0',
			  'tqdm==4.14',
			  'umap-learn==0.3.8',
			  'xgboost==0.80',
			  'numba==0.37',
                           'llvmlite==0.22',
                           'grpcio==1.8.6',
                           'docutils==0.14',
                           'pillow==4.0'],
	include_package_data=True,
	entry_points={'console_scripts': ['drugnomeai=drugnome_ai.modules.main.__main__:main']}
)
