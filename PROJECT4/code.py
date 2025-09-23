#word guessing game
import random
easy=["cat","fat","don","loan","fast","dust"]
medium=["apple","mango","happy","launch","Time"]
hard=["language","python","project"]
print("WELCOME TO THE WORD GUESSING GAEM!\n")
level=input("CHOOSE THE DIFFICULTY LEVEL.\n").lower().strip()
if level=="easy":
    word=random.choice(easy)
elif level=="hard":
    word=random.choice(hard)
elif level=="medium":
    word=random.choice(medium)
else:
    print("invalid input! deafult to easy level,\n")
    word=random.choice(easy)
total_attempts=0
print("\n Guess the secret word \n",end="")
while True:
    user_guess=input("Guess the word\n").lower().strip()
    total_attempts+=1
    if user_guess==word:
        print("congrats! You guess the word right.\n")
        print(f"in {total_attempts}total attemtps ")
        break
    hint=""
    for i in range(len(word)):
        if i<len(user_guess) and user_guess[i]==word[i]:
            hint+=user_guess[i]
        else:
            hint+="_"
    print(f"hint{hint}")
            