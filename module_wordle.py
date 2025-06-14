import random as r

def give_random_word():
    return r.choice(['apple','bread','candy','dream','eagle','flame','grape','house','input','joker'])

def give_guesses_output(word, guess):
    wordLength = len(word)
    display = ['']*wordLength # creating a display which we will populate with characters and their parameters (correct/not)
    temp_dict = {k: word.count(k) for k in set(word)} #uhhh, yeah, I think it looks much cleaner than writing it all in sperarate lines. It is used so it marks the correct amount of letters
    for k in range(wordLength):# we have 2 separate loops as in wordle the first prioriy should always be - correct index and character
        if guess[k] == word[k]: #specific index
            display[k]=(f"[{guess[k]}]")# replaced the append wih fixed change, as the append just adds in the end
            temp_dict[guess[k]]-=1 #if the letter in the guess is in the secret_word, make the amount of apperences of that letter in the secret_word smaller by one

    for k in range(wordLength):
        if display[k] == '': #check if it hasnt been populated yet
            if guess[k] in word and temp_dict[guess[k]] != 0: #check if this character was already added to display
                display[k]=(f"({guess[k]})")
                temp_dict[guess[k]]-=1
            else:
                display[k]=(guess[k])
    return display

def get_correct_guess(guess, len):
    while len(guess)!=len: #added a while loop so that it doesnt decrease tries, because if we have a for loop and continue, it would decrease tries
        print("Wrong length. Expected the length of", len)
        guess = input(f"Attempt {i+1}/6 – Enter guess: ").lower()
        if guess == "stop": #added it here in case a user wants to quit after he inputed wrong length
            return "stop"
    return guess
