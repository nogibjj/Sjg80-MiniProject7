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
    #devops
    black==22.3.0
    click==8.1.3 
    pytest==7.1.3
    pytest-cov==4.0.0
    pylint==2.15.3
    boto3==1.24.87
    #web
    fastapi==0.85.0
    uvicorn==0.18.3
    #data
    pandas == 2.1.0
    
    #rust based linter
    ruff==0.0.284
    boto3==1.24.87
      ],
)
