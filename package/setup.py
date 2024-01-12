from setuptools import setup, find_packages

def requirements_from_file(file_name):
    return open(file_name).read().splitlines()

setup(
    name='package',
    packages=find_packages(),
    description = "tools for machine learning",
    author = "tanaka",
    install_requires=requirements_from_file('requirements.txt'),
)