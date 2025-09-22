# TAKE NEW GENERATOR
#import random module
import random
subject=["john cena","virat kohli","cristano Ronaldo","shah Rukh kan ","Micheal Jackson"]
actions=["launches brand in  ","dances with ","playing with ","cancels visit to  ","riding ","declares war on ","celebrates "]
places=["Kathmandu","Dhangadi","mahendranagar","in  cricket ground","taj mahal"]
# start the headline genration loop
while True:
    user_input=input("Do you want A headline \n").lower().strip()
    if user_input=="yes":
        sub=random.choice(subject)
        act=random.choice(actions)
        place=random.choice(places)
        headline=(f"BREAKING NEWS:{sub} {act} {place}")
        print(headline +"\n")
   
   
    elif user_input=="no":
        break
    else:
        print("please type YES or NO")
    
print("Thanks for using .have a fun day")