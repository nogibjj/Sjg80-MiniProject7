from setuptools import setup, find_packages

setup(
    name='my_tool',
    version='1.0',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'my_tool=my_script:main',
        ],
    },
    install_requires=[
        'argparse',
    ],
)
