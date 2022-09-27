!pip install apyori
#importing the libraries of pandas, numpy and matplot
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
dataset = pd.read_csv("Dataset_master.xlsx - Netflix Movie Recommendation Ec (1).csv")
#Reading the Comma Seperated Value(CSV) file consisting the data of Netflix movies
transactions = []
#created an empty list called as transactions for traversing the data
for i in range(0, 7460):
  transactions.append([str(dataset.values[i, j]) for j in range(0, 20)])
#traversing the entire data in the CSV file in the order of rows and columns
from apyori import apriori
movies = apriori(transactions = transactions, min_support = 0.03, min_confidence = 0.2, min_lift = 3, min_length = 2)
results = list(movies)
print(results)
#this line is optional which prints the raw data of the data.
def inspect(results):
  movie1 = [tuple(result[2][0][0])[0] for result in results]
  movie2 = [tuple(result[2][0][1])[0] for result in results]
  support = [result[1] for result in results]
  return list(zip(movie1, movie2, support))
final_result = pd.DataFrame(inspect(results), columns = ['Movie1', 'Movie2', 'Support'])
print(final_result)
