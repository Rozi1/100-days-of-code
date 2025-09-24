import random
from hangman_art import stages, logo, word_list as words # type: ignore

lives = 0
attempts = 0
chosen_word = random.choice(words)
#print(chosen_word)
placeholder = "_" * len(chosen_word)

correct_letters = []
game_over = False
print(logo)
print(placeholder)
while not game_over:
    display = ""
    guess = input("Guess a letter: ").lower()
    #print(guess)

    if guess in chosen_word:
        print("Correct!")
        for letter in chosen_word:
            if letter == guess:
                display += letter
                correct_letters.append(letter)
                print(stages[lives])
            elif letter in correct_letters:
                display += letter
                #print(stages[lives])
            else:
                display += "_"
            
        print(display) 
        if "_" not in display:
            game_over = True
            print("*********************You win!***********************")     
    else:
        print("Wrong!")
        lives += 1
        attempts += 1
        print(stages[lives])
        if lives == 6:
            game_over = True
            print("You lose! The word was:", chosen_word)