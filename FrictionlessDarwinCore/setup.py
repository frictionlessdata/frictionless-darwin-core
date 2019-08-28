from setuptools import setup

setup(
    name='fdwc',
    version='0.1',
    py_modules=['fdwc'],
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        fdwc=conveter:cli
    ''',
)
