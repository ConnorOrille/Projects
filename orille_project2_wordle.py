"""
This program is a word game in which the user must guess a randomly chosen word taken from a file of 5-letter USA words.
The user has 6 chances to guess the word and is given hints along the way.
When the user guesses a word, letters that are correctly in the right spot are lit up as green.
Letters that are correctly chosen but in the wrong spot are lit up as yellow.
Letters that are completely incorrect are printed out as grey.


File Name:orille_project1_wordle.py
Date:01/05/2023
Course: COMP1352
Assignment: Preclass Assignmnet 3
Collaborators: 1352 Instructors
Internet Sources: None
"""
from random import random

print(f'Welcome to Wordle! You have six chances to guess the five-letter word.')
with open(r"C:\\Users\\Connor\\Desktop\\DU_2022Q1\\2022_Q2\\COMP1352WINTER2023\\Projects\\Project_2\\usaWords.txt", "r") as a_file:
    m = [line.strip() for line in a_file if len(line) == 6]


"""
This function takes in compares both the guess and the correct answer and outputs a string
of letters that represent the colors that are printed out later on.
These colors help the player to figure out what the correct answer is.

"""
def compare(guess:str, target:str):
    #creates a list that is the length of the answer which consists of only Bs
    #this gives a blank slate because B denotes grey
    output = ['B' for i in range(len(target))]
    #checks for if any letter is in the correct place
    for index in range(len(target)):
        #if any letter is in the correct place, change the B in that spot to a G
        if guess[index] == target[index]:
            output[index] = "G"
            #change the target value to a B if the value is changed
            #this is done to stop looking at that value in case there are duplicate letters
            target = target.replace(guess[index], "B", 1)
#checks for if any letter is correctly chosen, but in the incorrect place
    for index in range(len(target)):
        #if the letter is found in the target string and the output hasn't been touched yet
        if guess[index] in target and output[index] == "B":
            #place a Y instead of a B
            output[index] = "Y"
            # again replace that value to a B in the target
            #This stops the program from checking duplicate values
            target = target.replace(guess[index], "B", 1)
    #return the list of letters that are output and combine it into a string
    return ''.join(output)



# print with yellow background
def print_yellow(s, end='\n'):
   print('\u001b[43;1m', end='')
   print(s, end=end)
   print('\033[0m', end='')

# print with grey background
def print_grey(s, end='\n'):
   print('\u001b[47;1m', end='')
   print(s, end=end)
   print('\033[0m', end='')

# print with green background
def print_green(s, end='\n'):
   print('\u001b[42;1m', end='')
   print(s, end=end)
   print('\033[0m', end='')

#randomly find a number using the amount of 5-letter values from the usaWords.txt
number = int(random()*4436)
#assigns that word to the variable word
word = str(m[number])
#sets a variable to stop the loop of guessing (six guesses)
y = 0
#sets a variable that will be used to check the amount of letters in the guessed word
count = 0
#makes a list that will be used to put the guessed words in
#this list will print out each guess on each consecutive line
guesses = []
#while loop that sets up six guesses for the player
while y < 6:
    #asks the user for a word
    guess = input(str('What is your guess? '))
    count = 0
    #checks to see if the guessed word is contained in the usa words dictionary
    for element in m:
        #if the guessed word is not in the dictionary, a message is printed out to notify the user
        if element != guess:
            count += 1
    if count == len(m):
        print('That word does not exist in our dictionary')

    else:
        #if the word does exist in the dictionary and is 6 letters long, it is added to the list of guesses
        guesses.append(guess)
        #adds one to the guess count
        y+= 1
        for i in range(y):
            #prints out each guess on each consecutive line
            print(f'Guess {i+1}: {guesses[i]} ', end = '')

            
            #checks through every guess each time a good guess is inputted
            #Uses the color functions to print out a color depending on the letter of the hint
            for j in range(len(guesses[i])):
                #if the the letter is G, print out the letter of the guess in green
                if compare(guesses[i], word)[j] == 'G':
                    print_green(f" {guesses[i][j]} ", end='')
                #if the letter is Y, print out the letter in yellow
                if compare(guesses[i], word)[j] == 'Y':
                    print_yellow(f" {guesses[i][j]} ", end='')
                #if the letter is B, print out the letter in grey
                if compare(guesses[i], word)[j] == 'B':
                    print_grey(f" {guesses[i][j]} ", end='')
                
            print()
                    
                    
                    
                
                
       
    #if the guess is 100% correct, print this message and win screen the viewer
    if guess == word:
        print('You win')
        #shows the amount of guesses it took to get the answer
        print(f'You got it in {y} guesses!')
        #stops the loop of guessing
        y+=10
        #if the user guesses wrong 6 times, this lose screen is shown and the correct answer is given.
if y == 6:
    print('You lose, you did not guess the word in 6 guesses.')
    print(f'The correct answer was {word}!')
    


        

    