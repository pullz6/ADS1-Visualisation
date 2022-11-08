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
    avg = five_star.mean()
    for i in five_star.index: 
        if five_star[i] > avg: 
            list_five_star.append("High")
        elif five_star[i] < avg: 
            list_five_star.append("low") 
        else: 
            list_five_star.append("avg")
    return list_five_star
    
def numeric_four_star(four_star,total_reviews): 
    list_four_star = []
    for i in four_star.index: 
        four_star_value = four_star[i] * total_reviews[i]
        list_four_star.append(four_star_value)
    return list_four_star

def numeric_three_star(three_star,total_reviews): 
    list_three_star = []
    for i in four_star.index: 
        three_star_value = three_star[i] * total_reviews[i]
        list_three_star.append(three_star_value)
    return list_three_star

def numeric_two_star(two_star,total_reviews): 
    list_two_star = []
    for i in two_star.index: 
        two_star_value = two_star[i] * total_reviews[i]
        list_two_star.append(two_star_value)
    return list_two_star

def numeric_one_star(one_star,total_reviews): 
    list_one_star = []
    for i in one_star.index: 
        one_star_value = one_star[i] * total_reviews[i]
        list_one_star.append(one_star_value)
    return list_one_star

#Main Programme
#===========================================================================
#Extracting required data and including them into variables 
df_amazonbooks = pd.read_csv('final_book_dataset_kaggle.csv')
df_amazonbooks.dropna(axis=0, how='any', thresh=0, subset=None, inplace=True)
df_amazonbooks.dropna(subset=['star5','star4','star3','star2','star1'])
df_amazonbooks.sort_values("n_reviews", inplace = True)
print(df_amazonbooks['star2'])
#Prices for books
price = df_amazonbooks['price']
#Number of pages in the book 
pages = df_amazonbooks['pages']
#The average rating of the book
rating = df_amazonbooks['avg_reviews']
#The number of 5 star ratings 
five_star  = df_amazonbooks['star5']
#The number of 4 star ratings 
four_star = df_amazonbooks['star4']
#The number of 3 star ratings 
three_star = df_amazonbooks['star3']
#The number of 2 star ratings
two_star = df_amazonbooks['star2']
#The number of 1 star ratings
one_star  = df_amazonbooks['star1']
#The number of reviews provided 
no_reviews = df_amazonbooks['n_reviews']

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
 
data = []
data.append(numeric_five_star(five_star, no_reviews))
data.append(numeric_four_star(four_star, no_reviews))
data.append(numeric_three_star(three_star, no_reviews))
data.append(numeric_two_star(two_star, no_reviews))
data.append(numeric_one_star(one_star, no_reviews))
print(data)
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

