from pathlib import Path
import os
import yaml



def allContributors():
    filename = Path(os.path.join('..','contributors.yml'))

    with open(filename, 'r') as file:
            return yaml.load(file.read())

def getContributorInfo(name):
    contributor_list = allContributors()
    return contributor_list[name]


def getAllContent():
    filename = Path('../content.yml')
    with open(filename, 'r') as file:
            return yaml.load(file.read())
