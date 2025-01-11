'''
The setup.py file is an essential part of packaging and 
distributing Python projects. It is used by setuptools 
(or distutils in older Python versions) to define the configuration 
of your project, such as its metadata, dependencies, and more
'''

from setuptools import find_packages,setup
from typing import List
def get_requirements() -> List[str]:
          """
          This function wil return the list of requirements
          """
          requirement_lst:List[str]=[]
          try:
                  with open('requirements.txt') as file:
                          lines = file.readlines()
                          for line in lines:
                                  requirement = line.strip()
                                  ## ignore the empty lines and -e .
                                  if requirement and requirement!= '-e .':
                                          requirement_lst.append(requirement)
          except FileNotFoundError:
                  print("requirement.txt file not found")
                  
          return requirement_lst

# print(get_requirements())
setup(
        name = "Network security",
        version= "0.0.1",
        author = "Porchelvan kpm",
        author_email = "porchelvankpm@gmail.com",
        packages = find_packages() ,
        install_requires = get_requirements()
)
