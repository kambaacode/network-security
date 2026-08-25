from setuptools import find_packages, setup
from typing import List



def get_requirements() -> List[str]:
    """
        
        This function  will return a list of requirements

    """
    requirements_list:list[str] = []
    try:
        with open("requirements.txt", 'r') as file:
            lines = file.readlines()

            for line in lines:
               requirement = line.strip()
               if requirement and requirement != '-e .':
                   requirements_list.append(requirement)
        return requirements_list
    
    except FileNotFoundError:
        print("requirements.txt is not found")

setup(
    name= "Network Security",
    version= "0.0.1",
    author= "Mohamed",
    author_email= "mohamed.ahmed353635@gmail.com",
    packages= find_packages(),
    install_requires= get_requirements()
)