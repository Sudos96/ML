from setuptools import find_packages, setup

from typing import List


def get_pack(file_path: str) -> List[str]:
    ''' this function will create list of requirements'''
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n", "") for req in requirements]
        if "-e ." in requirements:
            requirements.remove("-e .")
    return requirements


setup(
    name="mldemo",
    version='0.0.1',
    author='Sudipta',
    author_email="sudiptad354@gmail.com",
    packages=find_packages(),
    # install_requires=['pandas','numpy','seaborn']
    install_requires=get_pack('requirements.txt')
)