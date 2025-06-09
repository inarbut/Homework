import randWords #added an import

print("Welcome to Wordle!") #moved it to the top to not to be printed every time

while True: #added a total while loop

    secret_word = randWords.give_random_word().lower() #called a function to get a random word from that module and also added .lower() in case the word is uppercase
    #removed x, y, z as there was no need for them

    tries = 6
    secret_word_length = len(secret_word) #renamed wl to secret_word_length

    print("Guess the",secret_word_length,"-letter word. You have", tries, "tries. Type stop to stop")

    won = False #variable to print if you won or no
    totalBreak = False #variable for global stop
    for i in range(tries): #replaced a while loop with a for loop
        guess = input(f"Attempt {i+1}/6 – Enter guess: ").lower() #replaced tries to i, to handle any amount of tries

        if guess == "stop": #added a global break to stop the entire program without keyboardInterruption
            totalBreak = True
            break
        
        while len(guess)!=secret_word_length: #added a while loop so that it doesnt decrease tries, because if we have a for loop and continue, it would decrease tries
            print("Wrong length. Expected the length of", secret_word_length)
            guess = input(f"Attempt {i+1}/6 – Enter guess: ").lower()
            if guess == "stop": #added it here in case a user wants to quit after he inputted wrong length
                totalBreak = True
                break
        

        if guess==secret_word:
            print("You won!!!")
            won = True
            break

        
        display = ['']*secret_word_length#to handle the priority, and I think the list coprehension here looks pretty clean
        temp_dict = {k: secret_word.count(k) for k in set(secret_word)} #uhhh, yeah, I think it looks much cleaner than writing it all in sperarate lines. It is used so it marks the correct amount of letters
        for k in range(secret_word_length):# we have 2 separate loops as in wordle the first prioriy should always be - correct index and character
            if guess[k] == secret_word[k]: #specific index
                display[k]=(f"[{guess[k]}]")# replaced the append wih fixed change, as the append just add in the end
                temp_dict[guess[k]]-=1 #if the letter in the guess is in the secret_word, make the amount of apperences of that letter in the secret_word smaller by one

        for k in range(secret_word_length):
            if display[k] == '':
                if guess[k] in secret_word and temp_dict[guess[k]] != 0: #check if this character was already added to display
                    display[k]=(f"({guess[k]})")
                    temp_dict[guess[k]]-=1
                else:
                    display[k]=(guess[k])


        #removed junk
        print("Result:", *display) #removed list comprehension as it already a list and no need for modification, replaced .join with * for clearer output 
    if totalBreak == True:
        break
    elif won == False: #elif here, because if you dont put it, it will print that you won and what the secret word was after you stop
        print("You lose! The word was:", secret_word)