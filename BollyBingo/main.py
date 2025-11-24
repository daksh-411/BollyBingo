# importing required libraries
import random
import pandas as pd

# reading csv file and converting dataframe to a list of movies
df = pd.read_csv("BollyBingo\movie_list.csv")
movie_list = df.iloc[:,0].to_list()

movie = random.choice(movie_list)
#print(movie)
movie_length = len(movie)

# Display underscores on console (If movie title contains space, show it as it is, and replace letters with underscores)
display = []
for i in range(movie_length):
    if movie[i] == " ":
        display.append(" ")
    else:
        display.append("_")
print(" ".join(display))

# Guess the Movie
gameOver = False
attempts = 5

while not gameOver:
    guess = input("Guess a letter: ").lower()

    if guess in display:
        print(f"You have already guessed {guess}. Try Again.")

    for i in range(movie_length):
        letter = movie[i]
        if guess == letter:
            display[i] = guess
    print(" ".join(display))

    if guess not in movie:
        print(f"The letter {guess} is not in the movie name. You lost a life.")
        attempts -= 1

        if attempts == 0:
            print("You exhausted all the lives. You Lost")
            print(f"The Movie Title was {movie.title()}")
            print("\tG A M E  O V E R")
            gameOver = True

    if "_" not in display:
        print("You guessed the movie correctly. You Won")
        print(f"The Movie Title was {movie.title()}")
        print("\tC O N G R A T U L A T I O N S")
        gameOver = True