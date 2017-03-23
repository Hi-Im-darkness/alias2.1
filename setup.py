from setuptools import setup, find_packages

with open('README.rst', 'r') as f:
    readme = f.read()

with open('README.rst', 'r') as f:
    license = f.read()

setup(
    name='alias2',
    version='1.1',
    author='Hi Im darkness',
    author_email='nghthach98@gmail.com',
    description='A sample Python project',
    long_description=readme,
    license=license,
    packages=find_packages(exclude=['__pycache__']),
    package_data={'alias2': ['data/user.data']},
    install_requires=[
        'click',
    ],
    entry_points={
        'console_scripts': [
            'alias2=alias2.script.interface:init',
        ],
    },
)
