import re #import random expressions library

#readString wants a string passed in and will raise an error if arg is not a string
#will find all words that end with at and store them in ending
#ending will be sorted by words that are longer than 3 letters into filtered 
#the filtered list will be returned
def readString(toRead):
    if type(toRead) != str:
        raise TypeError("Argument is not a string!")
    
    ending = re.findall("[A-Za-z]*at\\b",toRead)#finds all words ending in 'at'
    filtered = filter(lambda x: len(x) > 3, ending)#filters the words if theyre longer than 3 characters
    return filtered

source = open('pg1342.txt')#read in the story
pride = source.read()#read the story into a string
readString(pride)#call the function
