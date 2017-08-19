from setuptools import setup, find_packages

with open('README.md', 'r') as f:
    readme = f.read()

with open('LICENSE', 'r') as f:
    license = f.read()

setup(
    name='alias2',
    version='1.2',
    author='Hi Im darkness',
    author_email='nghthach98@gmail.com',
    description='A sample Python project',
    long_description=readme,
    license=license,
    packages=find_packages(exclude=['__pycache__']),
    install_requires=[
        'click',
    ],
    entry_points={
        'console_scripts': [
            'alias2=alias2.interface:init',
        ],
    },
)
