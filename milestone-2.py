import random

word_list = ["watermelon", "kiwi", "grape", "apple", "banana"]
print(word_list)

word = random.choice(word_list)
print(word)

guess = input("Please guess a single letter: ")
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

if len(guess) == 1 and guess in alphabet:
    print("Good guess!")
else:
    print("Oops! That is not a valid input.")


