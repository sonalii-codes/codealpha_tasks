import random
#Lists of predefined words 
words = ["cat","tiger","elephant","flower","python"]

#select a random words
word = random.choice(words)

#create blanks
guessed_word = ["_"] * len(word)

guessed_letter = []
attempts = 6

print("===Welcome to hangman game===")

while attempts > 0 and "_" in guessed_word:
    print("\nWord:","" .join(guessed_word))
    print("Guessed Letters:"," ".join(guessed_letter))
    print("Remaining Attempts:",attempts)
    guess = input("enter a letter:").lower()

    #check valid input
    if len(guess) != 1 or not guess.isalpha():
        print("please enter only one alphabet")
        continue
    #Check if guess is correct 
    if guess in word:
        for i in range(len(word)):
            if word[i] == guess:
                guessed_word[i] = guess
            print("Correct!")
    else:
        attempts -= 1
        print("Wrong guess!") 

    # Game result
    if "_" not in guessed_word:
        print("\n Congratulations! You guessed the word:", word)
    else:
        print("\n Game over!")
        print("The corret word is :", word)                  