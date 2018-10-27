#!/usr/bin/python

##Hangman
## Computer chooses a word
## Player guesses the letters of the word

def validate(word):
    if word.isalpha():
        if len(word) == 1:
            word = word
        else:
            word = None
    else:
        word = None
    return word

word = "hangman"
#print(word)
wrong_count = 0
right_count = 0

#use set rather than list because set only contains unique values
correct_letters=set(word)

#for letter in word:
 #   if letter not in correct_letters:
  #      correct_letters.append(letter)

print(correct_letters)

correct_guesses=[]


while (wrong_count < 10):
        
    guess = input("Guess a letter: ")
    guess = validate(guess)
    if guess:

        print (guess)
    
        if guess in word:
            print("Success!")
            if guess not in correct_guesses:
                correct_guesses.append(guess)
                if correct_guesses == correct_letters:
                    print("You win!")
                    break
            else:
                print("Already guessed that letter!")
            print(correct_guesses)
        
        #right_count +=1
        #print ("Correct guesses: " + str(right_count))
        #break
        else:
            print("Bad luck")
            wrong_count +=1
            print ("Wrong guesses: " + str(wrong_count))
    else:
        print("Guess not valid")
