#!/usr/bin/python3
import sys
import urllib

"""API usage"""
def API():
	"""Get user name and undone tasks list"""
	# getting user name
	oldUrl = "https://jsonplaceholder.typicode.com/users/"
	url = oldUrl + sys.argv[1]
	print(url)



if __name__ == "__main__":
	API()
