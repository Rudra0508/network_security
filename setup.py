from setuptools import setup,find_packages
from typing import List

def get_requirements()->List[str]:
    """ this functions will return the list of requirements"""
    
    requirement_list:List[str]=[]
    try:
        with open("requirements.txt","r")as file:
            #read lines from the file
            lines=file.readlines()
            #procssing each line
            for line in lines:
                requirement=line.strip()
                #ignore empty line and -e.
                if requirement and requirement!="-e .":
                    requirement_list.append(requirement)

    except FileNotFoundError:
        print("requirements.txt file not found")    
    
    return requirement_list


setup(
    name= "network_security_project",
    version="0.0.1",
    author="Rudra Pahuja",
    author_email="talktorudrapahuja@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements()
)