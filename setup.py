from setuptools import setup, find_packages

setup(
    name='tsr_package',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'pandas',
        'requests',
        'joblib',
    ],
    entry_points={
        'console_scripts': [
            'tsrkeygeneration=tsrkeygeneration.tsrkeygeneration:main',
        ],
    },
)
