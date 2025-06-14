import module_wordle #added an import

print("Welcome to Wordle!") #moved it to the top to not to be printed every time


def play():
    secret_word = module_wordle.give_random_word().lower() #called a function to get a random word from that module and also added .lower() in case the word is uppercase
    #removed x, y, z as there was no need for them

    tries = 6
    secret_word_length = len(secret_word) #renamed wl to secret_word_length

    print("Guess the",secret_word_length,"-letter word. You have", tries, "tries. Type stop to quit")

    for i in range(1, tries+1): #replaced a while loop with a for loop

        guess = module_wordle.get_correct_guess(secret_word_length, i)

        if not guess:
            return False

        if guess==secret_word:
            print("You won!!!")
            return True
        
        display = module_wordle.give_guesses_output(secret_word, guess)

        #removed junk
        print("Result:", *display) #removed list comprehension as it already a list and no need for modification, replaced .join with * for clearer output 
    print("You lose! The word was:", secret_word)
    return True

while True:
    if not play():
        break