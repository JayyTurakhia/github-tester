import yaml
import sys
FILENAME = '.github/dockerMeta/dockerDetails.yml'

def populateValues():
	with open(FILENAME) as file:
		data:dict = yaml.full_load(file)
		return data
details = dict()
details = populateValues()
