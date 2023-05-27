# Hangman-Project
This is my python coded version of the Hangman game 

## milestone-2.py file
- I created a variable named word_list that contained five fruit names in a list
- I created a word variable and using the random module (specifically random.choice function) to randomly generate a word from the word_list and assign it to the word variable 
- I made a input called guess which asks the user for a letter 
- I then made if and else statements to make sure the input was one letter and that the input was in the alphabet

## milestone-3.py file
- I created a function called check_guess, which contains if and else statements to check if the input guess is in the random word. 
- I created a ask_for_input function, which contains a while loop that asks for a valid guess. In order to test if the guess is valid I used an if and else statement. 

## milestone-4.py file
- Created Hangman class. Defined the following attributes: word_list, num_lives, list_of_guesses, word, word_guessed, num_letters. 
- Created methods within class called check_guess and ask_for_input. They act accordingly based on input to add or take away from the attributes and make the game work. 
