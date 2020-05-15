""" 

Group 5 Project for Problem Solving and Algorithms Mini Project titled 'Anagrams'

Group Members:
Tamunokorite Victor Briggs 191212016
Efemena Hilda Onovre
David Utee Usiere
Fatima Hyfa Abubakar
Mohammed Abdullahi Jibril

This code:
1, Reads words from a file chosen by the user;
2, Finds words that are anagrams of each other;
3, Outputs the group of words that form the most anagrams;
4, Outputs the largest Anagram.

"""

# import python modules that are needed in the code
from collections import defaultdict
import time

# function to check if two words are anagrams of each other
def is_anagram(firstWord, secondWord):
    firstWord = sorted(firstWord.lower())
    secondWord = sorted(secondWord.lower())
    if firstWord == secondWord:
        return True
    else:
        return False

# prompt the user to enter the filename and file extension, read the file and read each word on a new line
userFile = input("Enter filename and extension: ")

openFile = open(userFile, "r").read()

wordlist = [x.lower() for x in openFile.split("\n")]

# create a dictionary to store anagrams and their words
anagrams = defaultdict(list)
start = time.time()


# loop through the wordlist for word A; check A against all other words in the wordlist to see if they are anagrams of A; if any match is found, add it to the anagram list A belongs to 
for word1 in wordlist:
    firstWord = "".join(sorted(word1))
    for word2 in wordlist:
        secondWord = "".join(sorted(word2))
        if is_anagram(firstWord, secondWord):
            if word2 not in anagrams[firstWord]:
                anagrams[firstWord].append(word2)
            else:
                continue
        else:
            continue


# function to check the anagram dictionary and find the key with the most values(Largest Anagram)
def largest_anagram(anagramList):
    keyCount = defaultdict(list)
    for key in anagramList:
        values = [value for value in anagramList]
        valueCount = len(values)
        keyCount[key].append(valueCount)
    maxKey = max(keyCount, key = keyCount.get)
    return maxKey
largest_anagram = largest_anagram(anagrams)

# Output the group of words that form the most anagrams and output the largest anagram
print("The group words that form the most anagrams is " + str(anagrams[largest_anagram]) + "\n\n" + "The largest anagram is " + largest_anagram)
stop = time.time()
timeTaken = round(stop - start, 2)

if timeTaken == 1:
    print("Time Taken: " + str(timeTaken) + "second")
else:
    print("Time Taken: " + str(timeTaken) + "seconds")