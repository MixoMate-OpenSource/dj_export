from setuptools import setup

setup(
    name='dj_export',
    version='1.0',
    packages=['dj_export', 'dj_export.models'],
    install_requires=[
        'Django>=3.2',
        'polars>=1.4.1',
    ],
    author='Mixomate',
    author_email='chandrabhanvns@gmail.com',
    description='A Django package for exporting data to Excel and CSV',
    python_requires='>=3.6',
)