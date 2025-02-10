from setuptools import setup, find_packages


setup(
    name='lenexpy',
    description='LenexPY handler for MEET Entry Editor',
    version='0.0.6',
    install_requires=[
        'xmlbind'
    ],
    packages=find_packages(),
    # package_dir={'spherical_functions': '.'},
    # data_files=[('lenexpy', ['FINA_Points_Table_Base_Times.xlsx'])]
)
