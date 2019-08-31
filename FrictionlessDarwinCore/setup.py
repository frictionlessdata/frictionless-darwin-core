from setuptools import setup

setup(
    name='fdwca',
    version='0.1',
    py_modules=['fdwca'],
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        fdwca=fdwca:cli
    ''',
)
