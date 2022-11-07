#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov  6 10:05:18 2022

@author: Pulsara
"""

#Importing modules
#===========================================================================
import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt

#Functions
#===========================================================================
def price_to_gbp(price):
    price_in_gbp = []
    for one in price: 
        temp = one*0.88
        price_in_gbp.append(temp)
    return price_in_gbp

def numeric_five_star(five_star,total_reviews): 
    list_five_star = []
    
    
    

#Main Programme
#===========================================================================
#Extracting required data and including them into variables 
df_amazonbooks = pd.read_csv('final_book_dataset_kaggle.csv')
df_amazonbooks.sort_values("n_reviews", inplace = True)
#Prices for books
price = df_amazonbooks['price']
#Number of pages in the book 
pages = df_amazonbooks['pages']
#The average rating of the book
rating = df_amazonbooks['avg_reviews']
#The number of 5 star ratings 
five_star = rating = df_amazonbooks['star5']
print(df_amazonbooks['star5'].dtypes)
print(five_star) 
#The number of 4 star ratings 
four_star = rating = df_amazonbooks['star4']
print(df_amazonbooks['star4'].dtypes)
#The number of 3 star ratings 
three_star = rating = df_amazonbooks['star3']
#The number of 2 star ratings
two_star = rating = df_amazonbooks['star2']
#The number of 1 star ratings
one_star = rating = df_amazonbooks['star1']
#The number of reviews provided 
no_reviews = df_amazonbooks['n_reviews']
print(df_amazonbooks['n_reviews'].dtypes)

#Visualisation 
#Plotting a line graph 
fig, ax1 = plt.subplots()
color = "red"
ax1.set_xlabel('Number of Reviews')
ax1.set_ylabel('Rating', color=color)
ax1.plot(no_reviews, rating, color=color)
ax1.tick_params(axis='y', labelcolor=color)

ax2 = ax1.twinx()
color = "blue" 
ax2.set_ylabel('Price', color=color)
price_in_gbp = price_to_gbp(price)
ax2.plot(no_reviews, price_in_gbp, color=color)
ax2.tick_params(axis='y', labelcolor=color)
fig.tight_layout()
plt.show()


#Plotting a a histogram 
data = [five_star,four_star,three_star,two_star,one_star]
labels = ["5 Star Rating","4 Star Rating","3 Star Rating","2 Star Rating","1 Star Rating"]
plt.figure()
plt.subplots_adjust(hspace=0.6, wspace=0.6)
i=0
for i in range(len(data)):
    plt.subplot(2, 3, i+1)
    plt.hist(data[i])
    plt.xlabel("% of "+labels[i])
    plt.ylabel("Number of reviews")
    
plt.show()

#Plotting a violin plot 
plt.figure
# we need the subplot to get access to the axes object
fig, ax = plt.subplots(1, 1)
plt.violinplot(data, showmedians=True) # list with returns data from above
ax.set_xticks([1, 2, 3, 4,5])
ax.set_xticklabels(labels)
plt.ylabel("Ranges")
plt.savefig("violines.png")
plt.show()
