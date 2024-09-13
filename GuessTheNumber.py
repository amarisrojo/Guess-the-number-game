"""
script: GuessTheNumber
action: allows player to guess a random number, display needed hints, play again
author: Amaris Rojo
date: 08/30/2024
"""
#import random module to pick number
import random 

'''
action:generates random number, evaluate number entered, evaluate number of guesses

input:the players guess (as float)
output:Welcomes the player, gives hint to player based on number guessed 
return:number of guesses 
'''
#define main gain function
def guessingGame():
#generate number between (1,1000) 
    number = random.randint(1, 1000)

#count number of guesses 
    guessCount = 0

#INTRO,ask player for guess
    print('''Welcome Player!
Guess my number between 1 and 1000 with the fewest guesses!''' )

#create while loop to handle players guess, respond accordingly
#keep track of guesses
    while True:
        try:
            guess = int(input('Enter your guess: '))
            guessCount += 1

            #if number is too high 
            if guess > number:
                print('Too high. Try again.')
            #if number is too low 
            elif guess < number:
                print('Too low. Try again.')
            #if number is correct display
            else:
                print("Congratulations. You guessed the number!")

            #If the number is 10 or fewer
                if guessCount <= 10:
                    print("Either you know the secret or you got lucky!")

            #If the player makes more than 10 guesses
                else:
                    print("You should be able to do better!")
            #continue to display guess amount 
                return guessCount
        #make sure no invalid input is taken
        except ValueError:
            print('Invalid Input. Try entering a whole number.')

'''
action: run guessCount funtion, repeats/ends game, 

input:does player want to play again(yes or no)
output:prints number of guesses, asks player if they'd like to play again, Good-bye message
return: none
'''
#create main function, run the guessingGame function
#ask user if they want to play again, if not, end game
def main():
    while True:
        guessCount = guessingGame()
        print(f"You made {guessCount} guesses.")
        
        play_again = input("Do you want to play again? (1 = YES and 2 = NO): ")
        if play_again != '1':
            print("Thank you for playing. Hope to see you soon!")
            break

#call main
if __name__ == "__main__":
    main()