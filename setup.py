from setuptools import find_packages,setup
from typing import List
HYPEN_E_DOT='-e .'

def get_req(file_path :str)->List[str]:
    require = []

    with open(file_path)as file_obj:
        require = file_obj.readlines()
        require=[req.replace("\n"," ")for req in require]
        if HYPEN_E_DOT in require:
            require.remove(HYPEN_E_DOT)

    return require


setup(name='mlproject',
      version='0.0.1',
      author="sarthak",
      author_email="sarthaktyagi1704@gmail.com",
      packages=find_packages(),
      install_requires=get_req("requirement.txt")
      
      )



