from setuptools import setup, find_packages
from typing import List

def get_requirements()-> List[str]:
    """
    This function is going to take requirements.txt 
    return : this will return the list of all the libraries which is present in input file 
    """
    with open("requirements.txt") as req_file:
        return req_file.readlines().remove("-e .")


# python setup.py install will install the packages that has been given 
setup(
    name= "housing_prediction",
    version= "0.0.1",
    author= "Amit Thakur"
    description= "This is the revesion of the package creation",
    packages=find_packages() #["housing_pred"] this lib will search all the packages having init and return
    install_requires = get_requirements()
    )