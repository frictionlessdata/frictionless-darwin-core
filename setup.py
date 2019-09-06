from setuptools import setup, find_packages

setup(
    name='FrictionlessDarwinCore',
    version='0.1',
    author='André Heughebaert',
    license='MIT License',
    description='A tool converting Darwin Core Archive into Frictionless Data Package.',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'requests==2.22.0',
        'Click==7.0'
    ],
    entry_points='''
        [console_scripts]
        fdwca=FrictionlessDarwinCore.fdwca:cli
    ''',
)
