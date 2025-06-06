import random
words=["apple","banana","blueberry","cherry","kiwi","guava","watermelon","strawberry"]
chosen_word=random.choice(words)
attempts=6

print("Welcome to Hangman")
print("You have",attempts," attempts to guess the word")
print("All the best")

display=[]
for letter in chosen_word:
    display+='_'
print(display)

while attempts>0 and '_' in display:
    guess=input("Enter character to guess:").lower()
    if guess in chosen_word:
        for i in range(len(chosen_word)):
            if chosen_word[i]==guess:
                display[i]=guess
        print(display)
    else:
        attempts-=1
        print("Incorrect Guess")
        print("You have",attempts,"attempts left")
        print(display)
if '_' not in display:
    print("Congratulations!! The word is",chosen_word)
else:
    print("Better Luck Next Time, the word was",chosen_word)