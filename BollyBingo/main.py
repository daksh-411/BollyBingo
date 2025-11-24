# importing required libraries
import random
import pandas as pd

# reading csv file and converting dataframe to a list of movies
df = pd.read_csv("BollyBingo\movie_list.csv")
movie_list = df.iloc[:,0].to_list()

