from setuptools import find_packages, setup
from typing import List

h ='-e .'
def get_requirements(file_path:str)->List[str]:
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","")for req in requirements]
        if h in requirements:
            requirements.remove(h)
    return requirements
    
setup(
    name='mlproject',
    version='0.0.1',
    author='deva',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)