"""
Counts the number of individual words in a string. 
For added complexity read these strings in from a text file and generate a summary.
"""

string = raw_input("Enter a few words or so: ")

words = string.split()

print len(words)