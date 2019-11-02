from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='FrictionlessDarwinCore',
    version='0.2.0',
    author='André Heughebaert',
    author_email='andrejjh@gmail.com',
    license='MIT License',
    description='A tool converting Darwin Core Archive into Frictionless Data Package.',
    long_description=long_description,
    long_description_content_type="text/markdown",
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
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)
