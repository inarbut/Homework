import random as r

class bcolors: #this was pasted from the internet, it is used to give a better visual feedback
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def give_random_word():
    return r.choice(['apple','bread','candy','dream','eagle','flame','grape','house','input','joker'])

def give_guesses_output(word, guess):
    wordLength = len(word)
    display = ['']*wordLength # creating a display which we will populate with characters and their parameters (correct/not)
    temp_dict = {k: word.count(k) for k in set(word)} #uhhh, yeah, I think it looks much cleaner than writing it all in sperarate lines. It is used so it marks the correct amount of letters
    for k in range(wordLength):# we have 2 separate loops as in wordle the first prioriy should always be - correct index and character
        if guess[k] == word[k]: #specific index
            display[k]=(bcolors.OKGREEN + f"[{guess[k]}]" + bcolors.ENDC)# replaced the append wih fixed change, as the append just adds in the end
            temp_dict[guess[k]]-=1 #if the letter in the guess is in the secret_word, make the amount of apperences of that letter in the secret_word smaller by one

    for k in range(wordLength):
        if display[k] == '': #check if it hasnt been populated yet
            if guess[k] in word and temp_dict[guess[k]] != 0: #check if this character wasnt already added to display
                display[k]=(bcolors.WARNING + f"({guess[k]})" + bcolors.ENDC)
                temp_dict[guess[k]]-=1
            else:
                display[k]=(guess[k])
    return display

def get_correct_guess(leng, attempt):
    while True: #it is used to handle the incorrect length properly
        guess = input(f"Attempt {attempt}/6 – Enter guess: ").lower()#main guess function
        if guess == "stop":
            return False
        if len(guess) != leng: #checks if the length is correct
            print("Wrong length. Expected the length of", leng)
            continue #so it doesnt reach the final return guess line
        return guess
