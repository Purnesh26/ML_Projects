!pip install apyori
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
#importing the required libraries
dataset = pd.read_csv("Dataset_master.xlsx - Big Basket.com Cart Apriori (Pr.csv", header = None) 
#used for reading the Comma Seperated Value file consisting of different types of items customers have brought
transactions = []
for i in range(0, 7219):
  transactions.append([str(dataset.values[i, j]) for j in range(0, 20)])
#reading the data into an list
from apyori import apriori 
#used for importing the apriori for associative learning
basket_intelligence = apriori(transactions = transactions, min_support = 0.002, min_confidence = 0.2, min_lift = 3, min_length = 2)
#making the min_support for associative learning
results = list(basket_intelligence)
def inspect(results):
  product1 = [tuple(result[2][0][0])[0] for result in results]
  product2 = [tuple(result[2][0][1])[0] for result in results]
  support = [result[1] for result in results]
  confidence = [result[2][0][2] for result in results]
  lift = [result[2][0][3] for result in results]
  return list(zip(product1, product2, support, confidence, lift))
final_result = pd.DataFrame(inspect(results), columns = ['Product1', 'Product2', 'Support', 'Confidence', 'Lift'])
#used to display the top ten with largest lift values
final_result.nlargest(n = 10, columns = 'Lift')
