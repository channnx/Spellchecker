


import numpy
from spellCheckDictionary import getSpellCheckerDictionary

#get the dictionary stored in the spellCheckDictionary.py file
dictionary = getSpellCheckerDictionary()


#check if the give word is in the dictionary
def isAWord(word):
	return word in dictionary

#Check if a letter was mistakenly duplicated Ex: applle instead of apple
def duplicateLetterWord(word):
	tempWord = ""
	lastLetter = ""
	possibleWords = []
	#For each letter in the word
	for letter in word:
		#Check if the letter is the different than the previous letter
		if letter != lastLetter:
			#Add the non-duplicate letter to the new word
			tempWord += letter
		#The new last letter
		lastLetter = letter
	#If the new word is in the dictionary
	if isAWord(tempWord):
		#Add it to the possible word list
		possibleWords.append(tempWord)

	return possibleWords

#Check if a pair of adjacent letters are swapped Ex: taekn instead of taken
def swappedLetter(word):
	possibleWords = []
	#For each letter in the word
	for i in range(0, len(word)):
		#Create a new empty string
		newWord = ""
		x = 0
		#iterate over each letter in the word
		while x <= len(word) - 1:
			#If the index x is the same as the index i and the index x is not the last index of the string swap the next two letters
			if x == i and x < len(word) - 1:
				#Letter swap
				firstLetter = word[x]
				secondLetter = word[x+1]
				newWord += secondLetter + firstLetter
				#Increment the index x by 2 to skip the swapped letter
				x+=2
			#If this is not the index to swap
			else:
				#Add the letter
				newWord += word[x]
				#Increment the index x
				x+=1

		#Check if the new word with the two swapped letters is a valid word
		if isAWord(newWord):
			#If so add to the list of words
			possibleWords.append(newWord)

	return possibleWords


#Check if a word has an incorrect letter in it. Ex: impording instead of importing
def incorrectLetter(word):
	alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", ""]
	possibleWords = []
	#Iterate through all indexes of the word and alphabet
	for x in range(0, len(word)): #EVERY LETTER IN THE WORD
		for index in range(0, len(alphabet)): #EVERY LETTER IN THE ALPHABET
			#Create a new word with the letter at index x replaced with the alphabetic character at index index
			newWord = word[:x] + alphabet[index] + word[x+1:]
			#Check if the new word is a valid word
			if isAWord(newWord):
				#Add the valid word to the list
				possibleWords.append(newWord)
	return possibleWords

#Check if the word is missing a letter in it. Ex: titn instead of titan
def missingLetter(word):
	alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", ""]
	possibleWords = []
	#loop through letters of word
	for x in range(0, len(word)): #EVERY LETTER IN THE WORD
		for newLetter in alphabet: #EVERY LETTER IN THE ALPHABET
			#Create a new word with the newLetter at the index x
			newWord = word[:x] + newLetter + word[x:]
			#Check is the new word is a valid word
			if isAWord(newWord):
				#Add the valid word to the list
				possibleWords.append(newWord)
	return possibleWords

#Remove all non-alphabetic characters from a word and change the word to lowercase
def stripWord(word):
	#Create an empty string to hold the stripped word
	newWord = ""
	#For every letter in the original word
	for letter in word:
		#Check if the letter is an alphabetic character
		if letter.isalpha():
			#If so add it to the new word
			newWord += letter
	#Return the lowercase version of the new word
	return newWord.lower()

#Print the spellcheck suggestions based on the starting word and the list of possible corrections
def printResults(words, startingWord):
	#Create the starting part of the output 
	output = "You typed "+startingWord+". Did you mean "
	#Iterate over each word
	for x in range(0,len(words)):
		#If the word is the last word in the list and not the only word in the list
		if x == len(words)-1 and x != 0:
			#If so put an or before the word
			output += "or "
		#Add the new word to the output
		output += words[x]

		#If there are more than two words in the list
		if len(words) > 2:
			#Add a comma to the list
			output += ", "
		else:
			#Otherwise add a space instead
			output += " "

	#Once all words have been added to the output
	#If commas were added between each word
	if len(words) > 2:
		#Remove the last two characters, the comma and space after the comma
		output = output[:-2]
	else:
		#Otherwise just remove the last extra space after the last word.
		output = output[:-1]
	#Lastly add a questionmark to the end of the output
	output += "?"
	#Print the output
	print(output)


#SCRIPT

#Open the file that contains the sentences to check
file = open("checker.txt", "r")
#Create a new list that will contain all words in the file
words = []
#For each line in the file
for x in file:
	#Split the line into seperate words
	words += x.split()

#Store how many words are correct
corrcount = 0

#For each word in the file
for word in words:
	#Strip the word
	testWord = stripWord(word)
	#Check if the word exists in the dictionary
	if isAWord(testWord):
		#Increase the count of correct words by 1
		corrcount = corrcount + 1;
	#If the word is not in the dictionary check for the possible words
	else: 
		#Create a list to hold the possible words
		allPossibleWords = []
		#Check if the word has an extra duplicate letter
		allPossibleWords += duplicateLetterWord(testWord)
		#Check if the word has a swapped letter
		allPossibleWords += swappedLetter(testWord)
		#Check if the word has an incorrect letter
		allPossibleWords += incorrectLetter(testWord)
		#Check if the word is missing a letter
		allPossibleWords += missingLetter(testWord)

		#Temporarily convert the list to a set to remove duplicate results
		allPossibleWords = list(set(allPossibleWords))

		#If no checks returned any results
		if allPossibleWords == []:
			#Then the word has no close matches in the dictionary and the user is alerted that no suggestions are found
			print("Cannot find a suggestion for", testWord)
		else:
			#Print out the formated list of words that match the misspelled word
			printResults(allPossibleWords, testWord)

#Print out how many words are spelled correctly 
print('You spelt ' + str(corrcount) + ' words correctly')


